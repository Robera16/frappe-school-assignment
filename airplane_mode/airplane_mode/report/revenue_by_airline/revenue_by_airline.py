# Copyright (c) 2024, Robera Workneh and contributors
# For license information, please see license.txt

# Airline Revenue Report Script
import frappe
from frappe import _

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)

    summary = get_summary(data)

    chart = get_chart_data(data)

    return columns, data, None, chart, summary

def get_columns():
    return [
        {
            'fieldname': 'airline',
            'label': _('Airline'),
            'fieldtype': 'Link',
            'options': 'Airline',
            'width': 300
        },
        {
            'fieldname': 'revenue',
            'label': _('Revenue'),
            'fieldtype': 'Currency',
            'width': 150
        }
    ]

def get_data(filters):
    query = '''
        SELECT
            airline.name AS airline,
            SUM(ticket.total_amount) AS revenue
        FROM
            `tabAirplane Ticket` AS ticket
        JOIN
            `tabAirplane Flight` AS flight ON ticket.flight = flight.name
        JOIN
            `tabAirplane` AS airplane ON flight.airplane = airplane.name
        JOIN
            `tabAirline` AS airline ON airplane.airline = airline.name
        GROUP BY
            airline.name
        ORDER BY
            revenue DESC
    '''
    data = frappe.db.sql(query, as_dict=True)

    return data

def get_summary(data):
	
	total_revenue = sum([row['revenue'] for row in data])
	summary = [
        {
            'value': total_revenue,
            'label': _('Total Revenue'),
            'datatype': 'Currency',
        }
    ]

	return summary

def get_chart_data(data):
    labels = [row['airline'] for row in data]
    values = [row['revenue'] for row in data]

    chart = {
        'data': {
            'labels': labels,
            'datasets': [{'values': values}]
        },
        'type': 'donut'
    }

    return chart
