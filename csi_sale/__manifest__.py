# -*- coding: utf-8 -*-
{
    'name': "CSi Sale",
    'summary': "Customise sale order",
    'author': "Ankit H Gandhi",
    'version': "1.0",
    'category': "Sale",
    'website': "",
    'description': """
    Customise below point.
        * Only sales manager see 'SET TO QUOTATION' button(attributes).
    """ ,
    'depends': ['sale'],
    'data': ['views/inherit_sale_view.xml'],
    'auto_install':False,
    'installable':True,
    'application':True,
    # application
    # installable
}