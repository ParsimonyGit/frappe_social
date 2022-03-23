# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_social"
app_title = "Frappe Social"
app_publisher = "Parsimony LLC"
app_description = "App to contain social wall feature of frappe version 12 that works with frappe version-13"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@parsimony.com"
app_license = "GNU General Public License (v3)"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_social/css/frappe_social.css"
# app_include_js = "/assets/frappe_social/js/frappe_social.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_social/css/frappe_social.css"
# web_include_js = "/assets/frappe_social/js/frappe_social.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

boot_session = "frappe_social.boot.boot_session"
app_include_css = ["/assets/css/social.min.css"]
app_include_js = ["/assets/js/social.min.js"]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappe_social.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_social.install.before_install"
# after_install = "frappe_social.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_social.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_social.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_social.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_social.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_social.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_social.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_social.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_social.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_social.task.get_dashboard_data"
# }
