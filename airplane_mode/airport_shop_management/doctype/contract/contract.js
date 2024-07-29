// Copyright (c) 2024, Robera Workneh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Contract", {
	refresh(frm) {
        if (frm.is_new()){
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Shop Management Settings',
                    name: 'default_rent_amount'
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value('rent_amount', r.message.default_rent_amount);
                    }
                }
            });
        }
	},
});