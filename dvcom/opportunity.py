from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import today
import json
from frappe.desk.reportview import get_filters_cond
from functools import partial
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_material_request(source_name, target_doc=None):
    doclist = get_mapped_doc("Opportunity", source_name, {
                "Opportunity": {
                        "doctype": "Material Request",
                        "field_map": {
                                "name": "opportunity"
                        }
                },
                "Opportunity Item": {
                        "doctype": "Material Request Item",
                        "field_map": {
                                "uom": "stock_uom"
                        }
                }
        }, target_doc)
    return doclist
@frappe.whitelist()
def make_project(source_name, target_doc=None):
    doclist = get_mapped_doc("Opportunity", source_name, {
                "Opportunity": {
                        "doctype": "Project",
                        "field_map": {
                                "name": "opportunity"
                        }
                },
        }, target_doc)
    return doclist


