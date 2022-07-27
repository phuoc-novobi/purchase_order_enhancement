{
    'name': "Purchase Order Enhancement",
    'summary': "Enhance your purchase orders",
    'description': """ Purchase Order Enhancement module""",
    'author': "Phuoc Doan",
    'category': 'Tools',
    'version': '15.0',
    'depends': ['base', 'purchase', 'web'],
    'data': [
        'data/ir_cron_data.xml',

        'wizard/archive_purchase_order_view.xml',

        'report/purchase_order_templates.xml',
        'report/purchase_report_views.xml',

        'security/ir.model.access.csv',

        'views/purchase_views.xml',
        'views/res_config_settings.xml',
    ],
    'application': False,
    'assets': {
        'web.assets_backend': [
            'purchase_order_enhancement/static/src/js/purchase_phone_us_widget.js'
        ],
    },
}
