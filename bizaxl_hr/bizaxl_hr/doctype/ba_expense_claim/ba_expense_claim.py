import frappe
from frappe.model.document import Document
from frappe.utils import flt


class BAExpenseClaim(Document):
    def validate(self):
        self.calculate_totals()

    def calculate_totals(self):
        total_claimed = 0
        total_sanctioned = 0
        for exp in self.expenses:
            total_claimed += flt(exp.amount)
            total_sanctioned += flt(exp.sanctioned_amount or exp.amount)
        self.total_claimed_amount = total_claimed
        self.total_sanctioned_amount = total_sanctioned
