# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
from frappe import utils
from frappe.utils import date_diff

# import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"fieldname": "customer_name",
			"label": _("Opportunity Name"),
			"fieldtype": "Data",
			"width": 150

		},
		{
			"fieldname": "opportunity_type",
			"label": _("Opportunity_Type"),
			"fieldtype": "Link",
                        "options":"Opportunity Type",
                },
                {
                        "fieldname":"lead_owner",
                        "label":_("Lead Owner"),
                        "fieldtype":"Link",
                        "options":"User",
                 },
                 {
                        "fieldname":"sales_person",
                        "label":_("Sales Person"),
                        "fieldtype":"Link",
                        "options":"Sales Person",
                },  
		{
			"fieldname":"company_name",
			"label": _("Organization Name"),
			"fieldtype": "Link",
                        "options":"Lead",

		},
		{
			"fieldname":"transaction_date",
			"label": _("Date"),
			"fieldtype": "Date",
			"width": 150
		},
		{	"fieldname": "closing_date",
			"label": _("Closing Date"),
			"fieldtype": "Date",
			"width": 150

		},
		
		{
			"fieldname": "status",
			"label": _("Sales Stage"),
			"fieldtype": "Data",
			"width": 150
		},

		{
			"fieldname": "sales_stage",
			"label": _("Deal Status"),
			"fieldtype": "Data",
			"width": 150
		},
		{

			"fieldname": "source",
			"label": _("Lead Source"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "with_items",
			"label": _("With Items"),
			"fieldtype": "Check",
			"width": 150

		},
		{
			"fieldname": "item_code",
			"label": _("Item Code"),
			"fieldtype": "Data",
			"width": 150

		},
		{
			"fieldname": "qty",
			"label": _("Quantity"),
			"fieldtype": "Float",
			"width": 150
		}



		]

def get_conditions(filters):
    conditions = ""
	
    if filters.get("status"): conditions += "status = %(status)s and "
    if filters.get("from_date"): conditions += "transaction_date >= %(from_date)s"
    if filters.get("to_date"): conditions += " and transaction_date <= %(to_date)s"
    if filters.get("company"): conditions += " and company = %(company)s"
    if filters.get("lead_owner"): conditions += " and lead_owner = %(lead_owner)s"
    if filters.get("sales_person"): conditions += " and sales_person = %(sales_person)s"

    return conditions, filters		
			
def get_data(filters):

	data = []

	conditions, filters = get_conditions(filters)			

	
	details = frappe.db.sql('''select op.customer_name, op.opportunity_type,op.lead_owner, op.sales_person,op.company_name,op.transaction_date,op.closing_date,op.status,op.sales_stage,op.source,op.with_items,ab.item_code,ab.qty
        

			from `tabOpportunity` as op 
			inner join `tabOpportunity Item` as ab
			on op.name=ab.parent 
			    where %s order by status''' % conditions , filters, as_dict=1) 
                            
	print(details)
	for i in details:
		row = {

		"customer_name": i.customer_name,
		"opportunity_type": i.opportunity_type,
                "lead_owner":i.lead_owner,
                "sales_person":i.sales_person,
                "company_name":i.company_name,
		"transaction_date":i.transaction_date,
		"closing_date":i.closing_date,
		"status":i.status,
		"sales_stage":i.sales_stage,
		"source":i.source,
		"with_items":i.with_items,
		"item_code":i.item_code,
		"qty":i.qty
		}
		data.append(row)

	return data

                                           
	









