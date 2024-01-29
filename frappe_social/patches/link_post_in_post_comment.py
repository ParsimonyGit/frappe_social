import frappe


def execute():
	frappe.reload_doc("frappe_social", "doctype", "post_comment")
	comments = frappe.get_all("Post Comment", ["name", "parent"])
	for comment in comments:
		frappe.db.set_value("Post Comment", comment.name, "post", comment.parent)
