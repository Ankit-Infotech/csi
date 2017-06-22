# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    """ Hide Approve button, When current user look own time sheet """
    @api.depends('user_id')
    def _compute_own_user(self):
        for record in self:
            if record.user_id and record.user_id.id == self.env.uid:
                record.own_user = True
    """ End of code """

    own_user = fields.Boolean(compute='_compute_own_user', string='Check Own User') # Added new functional boolean field

