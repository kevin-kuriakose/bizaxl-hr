import frappe
from frappe.model.document import Document
from frappe.utils import date_diff, today


class BAEmployee(Document):
    def validate(self):
        self.validate_date_of_birth()
        if self.status == "Left" and not self.date_of_relieving:
            self.date_of_relieving = today()

    def validate_date_of_birth(self):
        if self.date_of_birth:
            age = date_diff(today(), self.date_of_birth) / 365
            if age < 18:
                frappe.throw("Employee must be at least 18 years old.")
