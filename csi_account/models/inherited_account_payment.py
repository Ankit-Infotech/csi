# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class account_payment(models.Model):
    _inherit = "account.payment"

    """ Override constrains """
    @api.one
    @api.constrains('amount')
    def _check_amount(self):
        if not self.amount >= 0.0:
            raise ValidationError('The payment amount must be strictly positive.')
    """ End of code """