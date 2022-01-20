// Copyright (c) 2016, craft interactive and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Pipeline Tracker"] = {
	"filters": [
	    {
			"fieldname":"status",
			"label": __("Status"),

			"fieldtype": "Select",

			"options":[
				"","Open","Quotation","Converted","Lost","Replied","Closed"
				
				//{ "value": "Open", "label": __("Open") },
				//{ "value": "Quotation", "label": __("Quotation") },
				//{"value":"Converted","label":__("Converted") },
				//{"value":"Lost","label":__("Lost") },
				//{"value":"Replied","label":__("Replied") },
				//{"value":"Closed","label":__("Closed") },
	   		 ],
	    },
	    {
			"fieldname": "from_date",
			 "label": __("From Date"),
			"fieldtype": "Date",
			"default":frappe.defaults.get_user_default("year_start_date"),

		},
		{
		 	 "fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default":frappe.datetime.get_today(),
		},

	    	{
	        	"fieldname":"company",
            		"label": __("Company"),
            		"fieldtype": "Link",
            		"options": "Company",
           	 	"default"  : "DVCOM TECHNOLOGY LLC",
	    	},

		{	
			"fieldname":"lead_owner",
			"label":__("Lead Owner"),
			"fieldtype":"Link",
			"options":"User",
		},
		{
			"fieldname":"sales_person",
			"label":__("Sales Person"),
			"fieldtype":"Link",
			"options":"Sales Person",
		}

	]
};

