{
    'name': 'My addon Odoo 14', 
    'sumary': "My addon",
    'website': "https://github.com/LucPinheiro",
    'description': 'My addon',
    'author': 'Lu Pinheiro', 
    'depends': ['base'], 
    'application': True, 
    'data': 
    [
        'security/ir.model.access.csv',
        'views/my_addon.xml',
        'views/my_addon_menu.xml'
    ]
}

