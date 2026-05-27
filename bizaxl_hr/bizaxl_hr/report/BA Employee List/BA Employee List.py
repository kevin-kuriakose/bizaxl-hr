import frappe
def execute(filters=None):
    filters = filters or {}
    columns = [
        {"fieldname": "name", "label": "Employee ID", "fieldtype": "Link", "options": "BA Employee", "width": 140},
        {"fieldname": "employee_name", "label": "Name", "fieldtype": "Data", "width": 180},
        {"fieldname": "department", "label": "Department", "fieldtype": "Link", "options": "BA Department", "width": 140},
        {"fieldname": "designation", "label": "Designation", "fieldtype": "Link", "options": "BA Designation", "width": 140},
        {"fieldname": "date_of_joining", "label": "Joining Date", "fieldtype": "Date", "width": 110},
        {"fieldname": "employment_type", "label": "Type", "fieldtype": "Data", "width": 100},
        {"fieldname": "status", "label": "Status", "fieldtype": "Data", "width": 80},
    ]
    conditions = "WHERE 1=1"
    values = {}
    if filters.get("department"):
        conditions += " AND department = %(department)s"
        values["department"] = filters["department"]
    if filters.get("status"):
        conditions += " AND status = %(status)s"
        values["status"] = filters["status"]
    if filters.get("company"):
        conditions += " AND company = %(company)s"
        values["company"] = filters["company"]
    data = frappe.db.sql(f"""
        SELECT name, employee_name, department, designation,
               date_of_joining, employment_type, status
        FROM `tabBA Employee`
        {conditions}
        ORDER BY employee_name
    """, values, as_dict=True)
    return columns, data
