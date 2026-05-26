import frappe
from frappe.model.document import Document
from frappe.utils import flt


class BALeaveAllocation(Document):
    def validate(self):
        self.total_leaves_allocated = flt(self.new_leaves_allocated) + flt(self.carry_forwarded_leaves)
