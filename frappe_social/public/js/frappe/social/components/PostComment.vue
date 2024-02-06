<template>
	<div>
		<div class="comment-box flex-column">
			<div class="comment-label text-muted">Add a comment</div>
			<div ref="commentsection"></div>
			<div class="flex justify-between comment-actions">
				<div class="text-muted small">Ctrl+Enter to add comment</div>
				<button class="btn btn-primary btn-sm" @click="create_comment">Comment</button>
			</div>
		</div>
		<div ref="commentlist" v-if="comments.length" class="comment-list">
			<div class="comment" v-for="comment in comments" :key="comment.name">
				<span
					class="cursor-pointer"
					@click="go_to_profile_page(comment.owner)"
					v-html="get_avatar(comment.owner)"
				>
				</span>
				<span class="content" v-html="comment.content" />
				<span class="text-muted" v-html="get_time(comment.creation)"> </span>
			</div>
		</div>
	</div>
</template>

<script setup>
import { onMounted, ref } from "vue";

const props = defineProps(["comments"]);
const emit = defineEmits(["create_comment"]);

const commentsection = ref(null);
const commentlist = ref(null);

onMounted(() => {
	make_comment_section();
	make_mentions_clickable(commentlist.value);
});

function get_avatar(user) {
	return frappe.avatar(user);
}

function get_time(timestamp) {
	return comment_when(timestamp, true);
}

function go_to_profile_page(user) {
	frappe.set_route("social", "profile", user);
}

function make_comment_section() {
	commentsection.value = frappe.ui.form.make_control({
		parent: commentsection.value,
		only_input: true,
		render_input: true,
		no_wrapper: true,
		enable_mentions: true,
		mentions: get_names_for_mentions(),
		df: {
			fieldtype: "Comment",
			fieldname: "comment",
		},
		on_submit: create_comment,
	});
}

function create_comment() {
	const message = commentsection.value.get_value().replace("<div><br></div>", "");
	if (!strip_html(message)) return;
	frappe.utils.play_sound("click");
	emit("create_comment", message);
	commentsection.value.clear();
}

function get_names_for_mentions() {
	let valid_users = Object.keys(frappe.boot.user_info).filter(
		(user) => !["Administrator", "Guest"].includes(user)
	);
	valid_users = valid_users.filter(
		(user) => frappe.boot.user_info[user].allowed_in_mentions == 1
	);
	return valid_users.map((user) => frappe.boot.user_info[user].name);
}

function make_mentions_clickable(parent_element) {
	const mentions = parent_element?.getElementsByClassName("mention") || [];
	Array.from(mentions).forEach((mention) => {
		mention.classList.add("cursor-pointer");
		mention.addEventListener("click", () => {
			go_to_profile_page(mention.dataset.value);
		});
	});
}
</script>

<style lang="less" scoped>
.comment-box {
	.comment-label {
		margin-bottom: 5px;
	}
	:deep(.ql-editor) {
		background: white;
		border-radius: 4px;
		min-height: 60px !important;
		border: 1px solid #d1d8dd;
	}
	.comment-actions {
		padding-top: 10px;
		button {
			padding: 2px 5px;
			font-size: 12px;
			align-self: flex-end;
		}
	}
}

.comment-list {
	margin-top: 10px;
	.comment {
		.comment-input-wrapper {
			margin-top: -6px;
			font-size: 11px;
		}
		display: flex;
		padding: 5px 0;
		.content {
			align-self: center;
			font-size: 12px;
			flex: 1;
		}
	}
}
</style>
