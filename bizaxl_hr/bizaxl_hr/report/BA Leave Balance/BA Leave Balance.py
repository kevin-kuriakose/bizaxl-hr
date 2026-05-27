import frappe
from frappe.utils import flt
def execute(filters=None):
    filters = filters or {}
    columns = [
        {"fieldname": "employee", "label": "Employee", "fieldtype": "Link", "options": "BA Employee", "width": 140},
        {"fieldname": "employee_name", "label": "Name", "fieldtype": "Data", "width": 180},
        {"fieldname": "leave_type", "label": "Leave Type", "fieldtype": "Link", "options": "BA Leave Type", "width": 140},
        {"fieldname": "total_leaves_allocated", "label": "Allocated", "fieldtype": "Float", "width": 100},
        {"fieldname": "leaves_taken", "label": "Taken", "fieldtype": "Float", "width": 100},
        {"fieldname": "balance", "label": "Balance", "fieldtype": "Float", "width": 100},
    ]
    conditions = "WHERE la.docstatus = 1"
    values = {}
    if filters.get("employee"):
        conditions += " AND la.employee = %(employee)s"
        values["employee"] = filters["employee"]
    if filters.get("leave_type"):
        conditions += " AND la.leave_type = %(leave_type)s"
        values["leave_type"] = filters["leave_type"]
    data = frappe.db.sql(f"""
        SELECT la.employee, e.employee_name, la.leave_type,
               la.total_leaves_allocated,
               COALESCE(SUM(app.total_leave_days), 0) as leaves_taken,
               la.total_leaves_allocated - COALESCE(SUM(app.total_leave_days), 0) as balance
        FROM `tabBA Leave Allocation` la
        LEFT JOIN `tabBA Employee` e ON e.name = la.employee
        LEFT JOIN `tabBA Leave Application` app
            ON app.employee = la.employee
            AND app.leave_type = la.leave_type
            AND app.docstatus = 1
        {conditions}
        GROUP BY la.employee, la.leave_type
        ORDER BY e.employee_name
    """, values, as_dict=True)
    return columns, data
