import frappe
from frappe.desk.doctype.notification_settings import (
	notification_settings as stock_notification_settings,
)

ROLE = "Bot Notification Admin"
_stock_get_permission_query_conditions = (
	stock_notification_settings.get_permission_query_conditions
)


def has_permission(doc, ptype="read", user=None):
	user = user or frappe.session.user
	if user != "Administrator" and ROLE in frappe.get_roles(user) and doc.name != "Administrator":
		return True
	return None


def get_permission_query_conditions(user=None):
	if not user:
		user = frappe.session.user

	# Administrator is reported as holding every Role. Leave that user on the stock path.
	if user != "Administrator" and ROLE in frappe.get_roles(user):
		return "(`tabNotification Settings`.name != 'Administrator')"

	return _stock_get_permission_query_conditions(user)


# Frappe ANDs every permission_query_conditions hook. Point the stock hook at
# this function so the role's condition is not intersected with `name = user`.
stock_notification_settings.get_permission_query_conditions = get_permission_query_conditions
