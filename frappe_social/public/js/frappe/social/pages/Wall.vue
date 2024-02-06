<template>
	<div class="wall-container">
		<post-sidebar class="post-sidebar hidden-xs"></post-sidebar>
		<div class="post-container">
			<div class="new_posts_count" @click="load_new_posts" v-show="new_posts_count">
				{{ new_posts_count + " new post" }}
			</div>
			<post-loader :post_list_filter="{}"></post-loader>
		</div>
		<activity-sidebar class="activity-sidebar hidden-xs" />
	</div>
</template>

<script setup>
import { onMounted, ref } from "vue";

import PostLoader from "../components/PostLoader.vue";
import PostSidebar from "../components/PostSidebar.vue";
import ActivitySidebar from "../components/ActivitySidebar.vue";

const emit = defineEmits(["load_new_posts"]);
const new_posts_count = ref(0);

onMounted(() => {
	frappe.realtime.on("new_post", (post_owner) => {
		if (post_owner === frappe.session.user) {
			load_new_posts();
		} else {
			new_posts_count.value += 1;
		}
	});
});

function load_new_posts() {
	emit("load_new_posts");
	new_posts_count.value = 0;
}
</script>
