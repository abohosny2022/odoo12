# -*- coding: utf-8 -*-
{
    'name': "Not enough inventory",

    'summary': """
        This app to hide message that show in order_lines when select a product which quantity is 		less than quantity on hand   """,

    'description': """
        This app to hide message that show in order_lines when select a product which quantity is 		less than quantity on hand
    """,

    'author': "Mohamed Hosny",
    'website': " ",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
