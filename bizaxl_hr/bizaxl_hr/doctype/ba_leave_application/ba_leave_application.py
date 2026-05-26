import frappe
from frappe.model.document import Document
from frappe.utils import date_diff, flt


class BALeaveApplication(Document):
    def validate(self):
        self.calculate_leave_days()

    def calculate_leave_days(self):
        if self.from_date and self.to_date:
            if self.half_day:
                self.total_leave_days = 0.5
            else:
                self.total_leave_days = date_diff(self.to_date, self.from_date) + 1

    def on_submit(self):
        self.status = "Open"
