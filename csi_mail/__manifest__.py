# -*- coding: utf-8 -*-

{
    'name': 'Mail Extend',
    'version': '1.0',
    'category': 'Mail',
    'sequence': 26,
    'summary': 'Mailing',
    'description': """
This module contain below feature:
----------------------------------
* Should be configuare outgoing mail server.
* Email would be send like @username in log an internal note.
    - condition like:
    - users_rec= self.env['res.users'].search([('name','=',username)]).
* Recipients email id will be display on chatter when send email button click.
* Example like:
    @Administrator do following things,
    1.Read docs.
    2.Analysis requirement.
    """,
    'author': 'Ankit H Gandhi',
    'website':'www.odoofun.com',
    'depends': ['mail'],
    'data': [],
    'demo': [],
    'installable': True,
    'application': True,
}