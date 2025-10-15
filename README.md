eezee_sale_order_extension/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── sale_order.py
└── views/
    └── sale_order_views.xml
This module displays the last open delivery date (last_open_delivery_date) in the sale order list view and highlights the row in red (decoration-danger) if the last open delivery date is older than 12 months.

Contents

models/sale_order.py: Contains the computed fields last_open_delivery_date and last_open_delivery_old, along with their computation logic.

views/sale_order_views.xml: Inherits the sale order tree view to add the new column and apply the decoration-danger style.

Installation

Copy the module folder into the Odoo addons directory.

Restart the Odoo server.

Activate the module from the Apps menu (you may need to enable Developer Mode).

Technical Notes

Depends on the sale_management and stock modules.

The last open delivery date is calculated using picking_ids and scheduled_date.

The “old” criterion = older than 12 months (this value can be adjusted).

License

MIT
