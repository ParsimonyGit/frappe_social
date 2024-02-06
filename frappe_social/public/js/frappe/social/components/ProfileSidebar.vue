<template>
	<div class="profile-sidebar flex flex-column">
		<div class="user-details">
			<h3>{{ user.fullname }}</h3>
			<p>
				<a @click="view_energy_point_list(user)" class="text-muted">
					Energy Points: {{ energy_points }}
				</a>
			</p>
			<p>{{ user.bio }}</p>
			<div class="location" v-if="user.location">
				<span class="text-muted">
					<i class="fa fa-map-marker">&nbsp;</i>
					{{ user.location }}
				</span>
			</div>
			<div class="interest" v-if="user.interest">
				<span class="text-muted">
					<i class="fa fa-puzzle-piece">&nbsp;</i>
					{{ user.interest }}
				</span>
			</div>
		</div>
		<a class="edit-profile-link" v-if="can_edit_profile" @click="edit_profile()">
			Edit Profile
		</a>
		<a class="edit-profile-link" v-if="can_edit_user" @click="edit_user()">User Settings</a>
	</div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const props = defineProps(["user_id"]);
const emit = defineEmits(["user_image_updated"]);

let user = frappe.user_info(props.user_id);
const can_edit_profile = frappe.social.is_session_user_page();
const can_edit_user = frappe.session.user === props.user_id;
const energy_points = ref(0);

onMounted(async () => {
	const response = await frappe.xcall(
		"frappe.social.doctype.energy_point_log.energy_point_log.get_user_energy_and_review_points",
		{ user: props.user_id }
	);

	energy_points.value = response[props.user_id]?.energy_points;
});

function edit_user() {
	frappe.set_route("Form", "User", props.user_id);
}

function edit_profile() {
	const edit_profile_dialog = new frappe.ui.Dialog({
		title: "Edit Profile",
		fields: [
			{
				fieldtype: "Attach Image",
				fieldname: "user_image",
				label: "Profile Image",
			},
			{
				fieldtype: "Data",
				fieldname: "interest",
				label: "Interests",
			},
			{
				fieldtype: "Column Break",
			},
			{
				fieldtype: "Attach Image",
				fieldname: "banner_image",
				label: "Banner Image",
			},
			{
				fieldtype: "Data",
				fieldname: "location",
				label: "Location",
			},
			{
				fieldtype: "Section Break",
				fieldname: "Interest",
			},
			{
				fieldtype: "Small Text",
				fieldname: "bio",
				label: "Bio",
			},
		],
		primary_action: (values) => {
			edit_profile_dialog.disable_primary_action();
			frappe
				.xcall("frappe.desk.page.user_profile.user_profile.update_profile_info", {
					profile_info: values,
				})
				.then((user) => {
					user.image = user.user_image;
					let user_info = frappe.user_info(props.user_id);
					user = Object.assign(user_info, user);
					emit("user_image_updated");
					edit_profile_dialog.hide();
				})
				.finally(() => {
					edit_profile_dialog.enable_primary_action();
				});
		},
		primary_action_label: "Save",
	});
	edit_profile_dialog.set_values({
		user_image: user.image,
		banner_image: user.banner_image,
		location: user.location,
		interest: user.interest,
		bio: user.bio,
	});
	edit_profile_dialog.show();
}

function view_energy_point_list(user) {
	frappe.set_route("List", "Energy Point Log", { user: user.name });
}
</script>

<style lang="less" scoped>
.profile-sidebar {
	padding: 10px 10px 0 0;
}

.user-details {
	.location,
	.interest {
		margin-bottom: 10px;
		i {
			width: 15px;
		}
	}
}

.edit-profile-link {
	margin-top: 15px;
}
</style>
