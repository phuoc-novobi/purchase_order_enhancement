{
    'name': "Purchase Order Enhancement",
    'summary': "Enhance your purchase orders",
    # 'description': """
    #     Manage Library
    #     ==============
    #     Description related to library.
    #     """,
    'author': "Phuoc Doan",
    'category': 'Tools',
    'version': '15.0',
    'depends': ['base', 'purchase'],
    'data': [
        'data/ir_cron_data.xml',
        'security/ir.model.access.csv',
        'views/purchase_views.xml',
        'views/res_config_settings.xml',
    ],
    'application': True,
    # 'demo': ['demo.xml'],
}
