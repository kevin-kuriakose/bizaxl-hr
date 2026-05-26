import frappe
from frappe.model.document import Document
from frappe.utils import time_diff_in_hours


class BAAttendance(Document):
    def validate(self):
        if self.in_time and self.out_time:
            self.working_hours = round(time_diff_in_hours(self.out_time, self.in_time), 2)
