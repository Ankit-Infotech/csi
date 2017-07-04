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

class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    # email id of the receipient will be appear in chatter # 1127
    @api.multi
    def get_mail_values(self, res_ids):
        partner_obj = self.env['res.partner']
        res = super(MailComposeMessage, self).get_mail_values(res_ids)
        Partners = False
        for res_id in res_ids:
            result = res[res_id]
            Partners = result.get('partner_ids')
            update_body = ''
            if Partners:
                for partner_rec in partner_obj.browse(Partners):
                    update_body += partner_rec.name +' :- '+ partner_rec.email + u'<br/>'
            if update_body:
                result.update({'body':update_body + result.get('body')})
        return res
    # End of code