from odoo import models, fields, api
from datetime import date

class SaleOrder(models.Model):
    _inherit = "sale.order"

    last_open_delivery_date = fields.Date(
        string="Last Open Delivery Date",
        compute="_compute_last_open_delivery_date",
        store=True
    )

    last_open_delivery_old = fields.Boolean(
        string="Delivery is Old",
        compute="_compute_last_open_delivery_date",
        store=True
    )

    @api.depends('picking_ids.scheduled_date', 'picking_ids.state')
    def _compute_last_open_delivery_date(self):
        for order in self:
            deliveries = order.picking_ids.filtered(lambda p: p.state not in ['done', 'cancel'])
            if deliveries:
                last_date = max(deliveries.mapped('scheduled_date'))
                order.last_open_delivery_date = last_date
                order.last_open_delivery_old = last_date.date() < date.today()
            else:
                order.last_open_delivery_date = False
                order.last_open_delivery_old = False
