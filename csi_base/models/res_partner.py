# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Partner(models.Model):
    _inherit = 'res.partner'

    # when EMAIL is populated, check for duplicates, WARN user "This email address is already in Odoo
    @api.onchange('email')
    def _onchange_email(self):
        email_count = 0
        warning = {}
        result = {}
        if self.email:
            email_count = self.search_count([('email','=',self.email)])
        if email_count >= 1:
            warning = {
                    'title': _('Warning!'),
                    'message': _('This email address is already in Odoo.'),
                }
        if warning:
            result['warning'] = warning
        return result
