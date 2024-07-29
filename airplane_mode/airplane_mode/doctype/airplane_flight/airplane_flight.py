# Copyright (c) 2024, Robera Workneh and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator, Document):
	def before_submit(self):
		self.set_status_completed()
	
	def set_status_completed(self):
		self.status = "Completed"
	
	def on_update_after_submit(self):
		tickets = frappe.get_all(
			"Airplane Ticket", 
			filters={"flight": self.name}, 
			fields=["name"]
    	)
		
		for ticket in tickets:
			frappe.db.set_value("Airplane Ticket", ticket.name, "gate_number", self.gate_number)



