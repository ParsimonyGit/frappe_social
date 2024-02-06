<template>
	<div>
		<div class="muted-title">Upcoming Events</div>
		<div class="event" v-for="event in events" :key="event.name">
			<span class="bold">{{ get_time(event.starts_on) }}</span>
			<a @click="open_event(event)"> {{ event.subject }}</a>
		</div>
		<div class="event" v-if="!events.length">No Upcoming Events</div>
	</div>
</template>

<script setup>
import { onMounted, ref } from "vue";

const events = ref([]);

onMounted(async () => {
	const _events = await get_events();
	events.value = _events;
});

async function get_events() {
	const today = frappe.datetime.now_date();
	return await frappe.xcall("frappe.desk.doctype.event.event.get_events", {
		start: today,
		end: today,
	});
}

function get_time(timestamp) {
	return frappe.datetime.get_time(timestamp);
}

function open_event(event) {
	frappe.set_route("Form", "Event", event.name);
}
</script>
