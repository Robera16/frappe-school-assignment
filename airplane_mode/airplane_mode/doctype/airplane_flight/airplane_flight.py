# Copyright (c) 2024, Robera Workneh and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator, Document):
	def before_submit(self):
		self.set_status_completed()
	
	def set_status_completed(self):
		self.status = "Completed"

