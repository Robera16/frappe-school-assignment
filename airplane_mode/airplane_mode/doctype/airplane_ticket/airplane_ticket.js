// Copyright (c) 2024, Robera Workneh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button('Assign Seat', function() {
            let d = new frappe.ui.Dialog({
                title: 'Enter Seat Number',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action_label: 'Set',
                primary_action(values) {
                    // Set the seat number field in the form
                    frm.set_value('seat', values.seat_number);
                    d.hide();
                }
            });

            d.show();
        }, 'Actions');
	},
});
