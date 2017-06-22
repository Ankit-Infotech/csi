# -*- coding: utf-8 -*-

{
    'name': 'Customise Account Module',
    'version':'1.0',
    'summary': 'Added some functionality of account module.',
    'description': """
        This module cover below point.
            - Override constrains of _check_amount.
            - Removed create and edit of partner from Bank Satement(Used attributes position have options parameter).
            - Removed crate and edit of partner from Bank Reconciliation(Web Part)
    """,
    'category': 'Account',
    'website':'',
    'author': 'Ankit H Gandhi',
    'depends': ['account'],
    'data': ['views/inherited_account_view.xml',
             'views/csi_account_web.xml',
             ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}