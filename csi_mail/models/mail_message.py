# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api, _, SUPERUSER_ID, tools

_logger = logging.getLogger(__name__)

class Message(models.Model):
    _inherit = 'mail.message'

    @api.model
    def create(self, vals):
        res = super(Message, self).create(vals)
        BODY = vals.get('body')
        if not BODY.find('@') == -1:
            username=BODY.split('@')[1].split(' ')[0]
            if username:
                users_rec= self.env['res.users'].search([('name','=',username)])
                if users_rec.partner_id.email:
                    body_html = "Hello," + '<br/>' + BODY.split('@')[1].split(' ',1)[1]
                    subject='Chatter message'
                    mail_values = {
                        'email_from':self.env.user.email,
                        'email_to':users_rec.partner_id.email,
                        'subject':subject,
                        'body_html':body_html,
                        'state':'outgoing',
                        'message_type':'email',
                    }
                    mail_id = self.env['mail.mail'].create(mail_values)
                    mail_id.send()
        return res