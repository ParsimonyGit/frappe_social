import frappe

ROLE = "Bot Notification Admin"


def has_permission(doc, ptype="read", user=None):
	if ptype not in ("read", "write"):
		return None

	user = user or frappe.session.user
	# Administrator is reported as holding every Role.
	if user != "Administrator" and ROLE in frappe.get_roles(user) and doc.name != "Administrator":
		return True
	return None
