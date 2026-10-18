# Copyright (c) 2026, Parsimony LLC and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

ROLE = "Bot Notification Admin"
BOT = "bot-notification-admin@example.com"
PLAIN = "plain-user@example.com"
OTHER = "other-user@example.com"


class TestBotNotificationAdmin(FrappeTestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		frappe.set_user("Administrator")
		_ensure_role()
		cls.bot = _ensure_user(BOT, [ROLE])
		cls.plain = _ensure_user(PLAIN)
		cls.other = _ensure_user(OTHER)
		_ensure_notification_settings("Administrator")
		_ensure_notification_settings(cls.bot)
		_ensure_notification_settings(cls.plain)
		_ensure_notification_settings(cls.other)

	def test_role_holder_can_read_and_write_another_users_settings(self):
		with self.set_user(self.bot):
			self.assertTrue(frappe.has_permission("Notification Settings", "read", self.other))
			self.assertTrue(frappe.has_permission("Notification Settings", "write", self.other))
			doc = frappe.get_doc("Notification Settings", self.other)
			doc.enabled = 0 if int(doc.enabled or 0) else 1
			doc.save()
			written = int(doc.enabled)

		saved = frappe.get_doc("Notification Settings", self.other)
		self.assertEqual(int(saved.enabled), written)

	def test_user_without_role_is_denied(self):
		with self.set_user(self.plain):
			self.assertFalse(frappe.has_permission("Notification Settings", "read", self.other))
			self.assertFalse(frappe.has_permission("Notification Settings", "write", self.other))
			doc = frappe.get_doc("Notification Settings", self.other)
			with self.assertRaises(frappe.PermissionError):
				doc.check_permission("read")
			with self.assertRaises(frappe.PermissionError):
				doc.save()

	def test_user_can_read_and_write_own_settings(self):
		with self.set_user(self.plain):
			self.assertTrue(frappe.has_permission("Notification Settings", "read", self.plain))
			self.assertTrue(frappe.has_permission("Notification Settings", "write", self.plain))
			doc = frappe.get_doc("Notification Settings", self.plain)
			doc.enabled = 0 if int(doc.enabled or 0) else 1
			doc.save()
			written = int(doc.enabled)
			names = frappe.get_list("Notification Settings", pluck="name", limit_page_length=0)
			self.assertEqual(names, [self.plain])

		saved = frappe.get_doc("Notification Settings", self.plain)
		self.assertEqual(int(saved.enabled), written)

	def test_administrator_settings_stay_blocked_for_role_holder(self):
		with self.set_user(self.bot):
			self.assertFalse(frappe.has_permission("Notification Settings", "read", "Administrator"))
			self.assertFalse(frappe.has_permission("Notification Settings", "write", "Administrator"))
			doc = frappe.get_doc("Notification Settings", "Administrator")
			with self.assertRaises(frappe.PermissionError):
				doc.check_permission("read")
			with self.assertRaises(frappe.PermissionError):
				doc.save()

	def test_get_list_returns_other_users_but_not_administrator(self):
		with self.set_user(self.bot):
			names = frappe.get_list("Notification Settings", pluck="name", limit_page_length=0)

		self.assertIn(self.other, names)
		self.assertIn(self.plain, names)
		self.assertNotIn("Administrator", names)


def _ensure_role():
	if frappe.db.exists("Role", ROLE):
		role = frappe.get_doc("Role", ROLE)
		if not int(role.desk_access or 0):
			role.desk_access = 1
			role.save(ignore_permissions=True)
		return

	frappe.get_doc(
		{"doctype": "Role", "role_name": ROLE, "desk_access": 1}
	).insert(ignore_permissions=True)


def _ensure_user(email, roles=None):
	roles = roles or []
	if frappe.db.exists("User", email):
		user = frappe.get_doc("User", email)
		existing = {row.role for row in user.roles}
		for role in roles:
			if role not in existing:
				user.append("roles", {"role": role})
		if roles:
			user.save(ignore_permissions=True)
		frappe.cache.hdel("roles", email)
		return email

	user = frappe.get_doc(
		{
			"doctype": "User",
			"email": email,
			"first_name": email.split("@", 1)[0],
			"send_welcome_email": 0,
			"roles": [{"role": role} for role in roles],
		}
	)
	user.insert(ignore_permissions=True)
	frappe.cache.hdel("roles", email)
	return email


def _ensure_notification_settings(user):
	if frappe.db.exists("Notification Settings", user):
		return
	doc = frappe.new_doc("Notification Settings")
	doc.name = user
	doc.insert(ignore_permissions=True)
