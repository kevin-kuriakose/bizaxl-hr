import frappe
def execute(filters=None):
    filters = filters or {}
    columns = [
        {"fieldname": "employee", "label": "Employee", "fieldtype": "Link", "options": "BA Employee", "width": 140},
        {"fieldname": "employee_name", "label": "Name", "fieldtype": "Data", "width": 180},
        {"fieldname": "department", "label": "Department", "fieldtype": "Data", "width": 140},
        {"fieldname": "attendance_date", "label": "Date", "fieldtype": "Date", "width": 100},
        {"fieldname": "status", "label": "Status", "fieldtype": "Data", "width": 100},
        {"fieldname": "in_time", "label": "In Time", "fieldtype": "Data", "width": 100},
        {"fieldname": "out_time", "label": "Out Time", "fieldtype": "Data", "width": 100},
    ]
    conditions = "WHERE docstatus = 1"
    values = {}
    if filters.get("employee"):
        conditions += " AND employee = %(employee)s"
        values["employee"] = filters["employee"]
    if filters.get("department"):
        conditions += " AND department = %(department)s"
        values["department"] = filters["department"]
    if filters.get("from_date"):
        conditions += " AND attendance_date >= %(from_date)s"
        values["from_date"] = filters["from_date"]
    if filters.get("to_date"):
        conditions += " AND attendance_date <= %(to_date)s"
        values["to_date"] = filters["to_date"]
    data = frappe.db.sql(f"""
        SELECT a.employee, a.employee_name, e.department,
               a.attendance_date, a.status, a.in_time, a.out_time
        FROM `tabBA Attendance` a
        LEFT JOIN `tabBA Employee` e ON e.name = a.employee
        {conditions}
        ORDER BY a.attendance_date DESC
    """, values, as_dict=True)
    return columns, data
