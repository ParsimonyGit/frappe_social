<template>
	<div ref="social" class="social">
		<keep-alive>
			<component
				:is="current_page.component"
				v-bind="current_page.props"
				@show_preview="toggle_preview(true)"
				@hide_preview="toggle_preview(false)"
			></component>
		</keep-alive>
		<image-viewer :src="preview_image_src" v-if="show_preview"></image-viewer>
	</div>
</template>

<script setup>
import { inject, onMounted, ref } from "vue";

import Wall from "./pages/Wall.vue";
import Profile from "./pages/Profile.vue";
import UserList from "./pages/UserList.vue";
import NotFound from "./components/NotFound.vue";
import ImageViewer from "./components/ImageViewer.vue";

function get_route_map() {
	return {
		"Social/home": {
			component: Wall,
			props: {},
		},
		"Social/profile/*": {
			component: Profile,
			props: {
				user_id: frappe.get_route()[2],
				key: frappe.get_route()[2],
			},
		},
		"Social/users": {
			component: UserList,
			props: {},
		},
		not_found: {
			component: NotFound,
		},
	};
}

let current_page = get_current_page();
const show_preview = ref(false);
const preview_image_src = ref("");
const social = ref(null);
const page = inject("page");

onMounted(() => {
	update_primary_action(frappe.get_route()[1]);

	frappe.router.on("change", () => {
		if (frappe.get_route()[0] === "Social") {
			set_current_page();
			update_primary_action(frappe.get_route()[1]);
			frappe.utils.scroll_to(0);
			$("body").attr("data-route", frappe.get_route_str());
		}
	});

	frappe.ui.setup_like_popover($(social.value), ".likes", false);
});

function toggle_preview(show) {
	preview_image_src.value = show ? src : "";
	show_preview.value = show;
}

function set_current_page() {
	current_page = get_current_page();
}

function update_primary_action(current_route) {
	if (current_route === "home") {
		page.set_title("Social");
		frappe.breadcrumbs.update();
		page.set_primary_action("Post", () => {
			frappe.social.post_dialog.show();
		});
	} else {
		frappe.breadcrumbs.add({
			type: "Custom",
			label: "Social Home",
			route: "#social/home",
		});
		page.clear_primary_action();
	}

	if (current_route === "users") {
		page.set_title("Leaderboard");
	}
}

function get_current_page() {
	const route_map = get_route_map();
	const route = frappe.get_route_str();

	if (route_map[route]) {
		return route_map[route];
	} else {
		return (
			route_map[route.substring(0, route.lastIndexOf("/")) + "/*"] || route_map["not_found"]
		);
	}
}
</script>
