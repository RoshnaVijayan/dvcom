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
	data = get_record(filters)
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
			"fieldname": "Opportunity Type",
			"label": _("opportunity_type"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "organization_name",
			"label": _("Organization Name"),
			"fieldtype": "Data",
			"width": 150

		},
		{
			"fieldname": "date",
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
			"fieldname": "country",
			"label": _("Country"),
			"fieldtype": "Data",
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

def get_record(filters):
	data = []
	

	details = frappe.db.sql('''select op.customer_name, op.opportunity_type,op.organization_name,op.transaction_date,op.closing_date,op.country, op.status,op.sales_stage,op.source,op.with_items,ab.item_code,ab.qty

			from `tabOpportunity` as op 
			inner join `tabOpportunity Item` as ab
			on op.name=ab.parent 
				where op.status = %s and op.transaction_date >= %s and op.transaction_date <= %s  and op.company = %s
				''',(filters.status,filters.from_date,filters.to_date,filters.company ), as_dict = 1)
	print(details)
	for i in details:
		row = {

		"customer_name": i.customer_name,
		"opportunity_type": i.opportunity_type,
		"organization_name":i.organizationa_name,
		"transaction_date":i.transaction_date,
		"closing_date":i.closing_date,
		"country":i.country,
		"status":i.status,
		"sales_stage":i.sales_stage,
		"source":i.source,
		"with_item":i.with_item,
		"item_code":i.item_code,
		"qty":i.qty
		}
		data.append(row)

	return data

