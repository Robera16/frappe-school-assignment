# Copyright (c) 2024, Robera Workneh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string

class AirplaneTicket(Document):

	def validate(self):
		self.validate_state()
		self.remove_duplicate_addons()
		self.calculate_total_amount()
		
	def validate_state(self):
		if self.status != "Boarded":
			frappe.throw('Status should be Boarded')

	def calculate_total_amount(self):
		self.total_amount = self.flight_price or 0
		for addon in self.add_ons:
			self.total_amount += addon.amount or 0

	def remove_duplicate_addons(self):
		unique_addons = []
		addon_items = set()
		for addon in self.add_ons:
			if addon.item not in addon_items:
				addon_items.add(addon.item)
				unique_addons.append(addon)
		self.add_ons = unique_addons

	def before_insert(self):
		self.set_random_seat()
	
	def set_random_seat(self):
       
		random_number = random.randint(1, 100)
		random_letter = random.choice(string.ascii_uppercase[:5])  
		self.seat = f"{random_number}{random_letter}"