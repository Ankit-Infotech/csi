# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, SUPERUSER_ID
from datetime import datetime, timedelta

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.one
    @api.depends('change_order_date')
    def _by_day_date_order(self):
        for purchase in self:
            DATE_ORDER_STR = purchase.date_order[:10]
            DATE_ORDER_DATE = datetime.strptime(DATE_ORDER_STR, "%Y-%m-%d")
            DATE_ORDER_ADD_ONE_WEEK_DATE = DATE_ORDER_DATE + timedelta(days=7)
            DATE_ORDER_ADD_ONE_WEEK_STR = DATE_ORDER_ADD_ONE_WEEK_DATE.strftime("%Y-%m-%d")
            self.write({'by_date': DATE_ORDER_STR, 'by_week':DATE_ORDER_STR +' To '+DATE_ORDER_ADD_ONE_WEEK_STR})

    change_order_date = fields.Boolean(string='Change date', compute='_by_day_date_order')
    by_date = fields.Char(string='By Date')
    by_week = fields.Char(string='By Week')

