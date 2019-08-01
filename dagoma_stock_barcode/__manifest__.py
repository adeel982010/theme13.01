# -*- coding: utf-8 -*-

{
    'name': "Dagome Barcode",
    'summary': "Dagoma customizations on barcode interface",
    'description': """
        This module adds required customizations for Dagoma on barcode interface.

        - Task 2029726
            Ease to increment product

        - Task 2026824
            Warnings on barcode use
    """,
    'category': 'Warehouse',
    'version': '1.0',
    'depends': ['stock_barcode'],
    'data': [
        'views/webclient_templates.xml'
    ],
    'qweb': [
        'static/src/xml/stock_barcode.xml'
    ]
}
