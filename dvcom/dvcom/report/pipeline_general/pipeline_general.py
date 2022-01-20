# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
from frappe import utils
from frappe.utils import date_diff

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
			"fieldname": "opportunity_type",
			"label": _("Opportunity Type"),
			"fieldtype": "Link",
            "options":"Opportunity Type",
        },
		{
			"fieldname": "organization_name",
			"label": _("Organization Name"),
			"fieldtype": "Data",
            "width":150
        },
		{
			"fieldname": "transaction_date",
			"label": _("Date"),
			"fieldtype": "Date",
			"width": 150
		},
		{
			"fieldname": "closing_date",
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
		}
	]


def get_record(filters):
	data = []
	details = frappe.db.sql('''
		select op.customer_name, op.opportunity_type,op.organization_name,op.transaction_date,
		op.closing_date,op.country, op.status,op.sales_stage,op.source 
		from `tabOpportunity` as op 
		where op.status = %s and op.transaction_date >= %s and op.transaction_date <= %s  and op.company = %s
		''',(filters.status,filters.from_date,filters.to_date,filters.company ), as_dict=1)
	for i in details:
		row = {
			"customer_name": i.customer_name,
			"opportunity_type": i.opportunity_type,
			"organization_name":i.organization_name,
			"transaction_date":i.transaction_date,
			"closing_date":i.closing_date,
			"country":i.country,
			"status":i.status,
			"sales_stage":i.sales_stage,
			"source":i.source
		}
		data.append(row)

	return data