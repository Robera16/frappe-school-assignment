// Copyright (c) 2024, Robera Workneh and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            
            // Add a web link to the sidebar
            const website = frm.doc.website;
            frm.add_web_link(website, "Visit Website");
        }
    }
});
