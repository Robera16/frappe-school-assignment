import frappe
import string
import random
from frappe.utils import nowdate


def monthly():
    shop_management_settings = frappe.get_single("Shop Management Settings")

    if shop_management_settings.enable_rent_reminders:

        contracts = frappe.get_all('Contract', filters={'end_date': ['>=', nowdate()]})
        for contract in contracts:
            single_contract = frappe.get_doc('Contract', contract.name)
            tenant = frappe.get_doc('Tenant', single_contract.tenant_email)
            if tenant.email:
                frappe.sendmail(
                    recipients=tenant.email,
                    subject='Rent Due Reminder',
                    message=f"""
                        <p>Dear {tenant.name1},</p>
                        <p>This is a reminder that your rent of <strong>{single_contract.rent_amount}</strong> is due. Please ensure that the payment is made by the due date to avoid any late fees.</p>
                        <p>Thank you!</p>
                        <p>Best regards,</p>
                        <p>Ethiopian Airlines</p>
                    """,
                    delayed=False,
                    retry=3 
                )