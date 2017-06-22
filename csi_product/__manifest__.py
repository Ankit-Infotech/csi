# -*- coding: utf-8 -*-
{
    'name': 'Product Customize',
    'version': '1.0',
    'category': 'Product',
    'summary': 'Customize product module',
    'description': """
This module cover below point:
------------------------------
* Total Re-Ordering rule create as per total number of warehouse, when product will be create.
* To change invoice policy based on Product Type Selection.(Used onchange method)
* Internal Reference(default_code)To be mandatory on Product if Product Type is Stockable Product.(attrs in xml)
    """,
    'website':'www.odoofun.wordpress.com',
    'author': 'Ankit H Gandhi',
    'depends': ['product'],
    'data': [
        'views/inherit_product_view.xml',
    ],
    'installable':True,
    'auto_install': False,
    'application':True,
}