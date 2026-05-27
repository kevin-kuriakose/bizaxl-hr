app_name = "bizaxl_hr"
app_title = "BizAxl HR"
app_publisher = "BizAxl"
app_description = "HR & People management for BizAxl ERP"
app_email = "dev@bizaxl.com"
app_license = "mit"
app_version = "1.0.0"

required_apps = ["frappe", "bizaxl_erp"]

fixtures = [
    {"doctype": "Workspace", "filters": [["name", "in", ["HR"]]]},
    {"doctype": "Notification", "filters": [["document_type", "in", [
        "BA Employee", "BA Leave Application", "BA Attendance", "BA Expense Claim"
    ]]]},
]
