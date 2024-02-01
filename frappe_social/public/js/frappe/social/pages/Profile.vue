<template>
	<div>
		<div class="profile-head">
			<profile-banner :user_id="user_id"></profile-banner>
		</div>
		<div class="profile-container">
			<profile-sidebar :user_id="user_id" class="profile-sidebar" />
			<div class="post-container">
				<div class="list-options">
					<div
						class="option"
						:class="{ bold: show_list === 'user_posts' }"
						@click="show_list = 'user_posts'"
					>
						<span>Posts</span>
						<span>({{ user_posts_count }})</span>
					</div>
					<div
						class="option"
						:class="{ bold: show_list === 'liked_posts' }"
						@click="show_list = 'liked_posts'"
					>
						<span>Likes</span>
						<span>({{ liked_posts_count }})</span>
					</div>
				</div>
				<post-loader :post_list_filter="post_list_filter"></post-loader>
			</div>
			<activity-sidebar class="activity-sidebar hidden-xs" />
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";

import PostLoader from "../components/PostLoader.vue";
import ProfileSidebar from "../components/ProfileSidebar.vue";
import ActivitySidebar from "../components/ActivitySidebar.vue";
import ProfileBanner from "../components/ProfileBanner.vue";

const props = defineProps(["user_id"]);
const show_list = ref("user_posts");
const post_list_filter = ref(null);
const user_posts_count = ref(0);
const liked_posts_count = ref(0);

watch(show_list, () => {
	if (show_list.value == "user_posts") {
		post_list_filter.value = get_user_posts_filter();
	} else if (show_list.value == "liked_posts") {
		post_list_filter.value = get_liked_posts_filter();
	}
});

onMounted(() => {
	post_list_filter.value = get_user_posts_filter();
	set_post_count();
});

function get_user_posts_filter() {
	return {
		owner: props.user_id,
	};
}

function get_liked_posts_filter() {
	return {
		liked_by: ["like", "%" + props.user_id + "%"],
	};
}

function set_post_count() {
	frappe.db
		.count("Post", { filters: get_user_posts_filter() })
		.then((count) => (user_posts_count.value = count));

	frappe.db
		.count("Post", { filters: get_liked_posts_filter() })
		.then((count) => (liked_posts_count.value = count));
}
</script>

<style lang="less" scoped>
.profile-head {
	height: 260px;
}

.profile-sidebar {
	margin-top: 60px;
	flex: 20%;
}

.right-sidebar {
	margin-top: 5px;
}

.list-options {
	display: flex;
	.option {
		cursor: pointer;
		padding: 0 10px 10px 0;
	}
}
</style>
