frappe.provide("frappe.social");

import { createApp } from "vue";
import Home from "./SocialHome.vue";

frappe.social.Home = class SocialHome {
	constructor({ parent }) {
		this.$parent = $(parent);
		this.page = parent.page;
		this.setup_header();
		this.make_body();
	}

	setup_header() {
		this.page.set_title(__("Social"));
	}

	make_body() {
		this.$social = this.$parent.find(".layout-main");
		const app = createApp(Home);
		app.config.globalProperties.page = this.page;
		app.mount(this.$social[0]);
	}
};

frappe.social.post_dialog = new frappe.ui.Dialog({
	title: __("Create Post"),
	fields: [
		{
			fieldtype: "Text Editor",
			fieldname: "content",
			label: __("Content"),
			reqd: 1,
		},
	],
	primary_action_label: __("Post"),
	primary_action: (values) => {
		frappe.social.post_dialog.disable_primary_action();
		const post = frappe.model.get_new_doc("Post");
		post.content = values.content;
		frappe.db
			.insert(post)
			.then(() => {
				frappe.social.post_dialog.clear();
				frappe.social.post_dialog.hide();
			})
			.finally(() => {
				frappe.social.post_dialog.enable_primary_action();
			});
	},
});

frappe.social.is_home_page = () => {
	return frappe.get_route_str() === "Social/home";
};

frappe.social.is_profile_page = (user) => {
	return (
		frappe.get_route()[0] === "Social" &&
		frappe.get_route()[1] === "profile" &&
		(user ? frappe.get_route()[2] === user : true)
	);
};

frappe.social.is_session_user_page = () => {
	return frappe.social.is_profile_page() && frappe.get_route()[2] === frappe.session.user;
};

frappe.provide("frappe.app_updates");
frappe.utils.make_event_emitter(frappe.app_updates);
