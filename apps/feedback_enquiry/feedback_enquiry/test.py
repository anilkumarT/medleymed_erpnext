@frappe.whitelist(allow_guest=True)
def ping():
    return "Test API success"