# -*- coding: utf-8 -*-

{
    'name': 'Csi Purchase Management',
    'version': '1.0',
    'category': 'Purchases',
    'sequence': 61,
    'summary': 'Customise in purchase module',
    'description': """
This module cover below point:
------------------------------
* Modified delete confirmation message(web).
* Added filter of group by date,1 week.
    """,
    'website': 'www.odoofun.wordpress.com',
    'depends': ['purchase'],
    'data': [
        'views/csi_purchase_web.xml',
        'views/csi_purchase_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}