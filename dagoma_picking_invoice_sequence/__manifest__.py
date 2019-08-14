# -*- coding: utf-8 -*-
{
    'name':        "Dagoma",

    'summary':
                   """
                   	Customization needed by Dagoma""",

    'description': """
        	Customization needed by Dagoma 
    """,

    'author':      "Odoo",
    'website':     "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':    'Uncategorized',
    'version':     '12.0.0.9',

    # any module necessary for this one to work correctly
    'depends':     ['base', 'delivery','website_sale_delivery'],

    # always loaded
    'data':        [
        "views/delivery_carrier_views.xml",
        "views/product_category_views.xml",
        "data/cron.xml",
        "data/sequence.xml"
    ],
    # only loaded in demonstration mode
    'demo':        [],
}
