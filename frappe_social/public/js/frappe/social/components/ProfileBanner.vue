<template>
	<div ref="banner" class="banner" :style="background_style">
		<div class="user-avatar container" v-html="user_avatar"></div>
	</div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps(["user_id"]);

const user_avatar = frappe.avatar(props.user_id, "avatar-xl");
const user_banner = frappe.user_info(props.user_id).banner_image;

const background_style = computed(() => {
	const style = {};
	if (user_banner) {
		style["background-image"] = `url('${user_banner}')`;
	}
	return style;
});
</script>

<style lang="less" scoped>
.banner {
	top: 0;
	left: 0;
	width: 100%;
	height: 300px;
	z-index: 101;
	position: absolute;
	background-size: cover;
	background-position: center;
	background-repeat: no-repeat;
	background-color: #262626;
	.user-avatar {
		position: relative;
		:deep(.avatar) {
			top: 220px;
			left: 10px;
			width: 150px;
			height: 150px;
			border-radius: 4px;
			background: white;
			position: absolute !important;
		}
	}
	.editable-image {
		:deep(.avatar) {
			cursor: pointer;
			:hover {
				opacity: 0.9;
			}
		}
	}
}
</style>
