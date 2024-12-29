{
    'name': "Apprendimento Odoo",
    'version': "1.0",
    'summary': "Modulo per apprendere l'utilizzo di Odoo attraverso tutorial ed esercizi guidati",
    'sequence': -100,
    'description': """Modulo interattivo per guidare i nuovi sviluppatori di Odoo nell'apprendimento delle funzionalità di base.""",
    'category': 'Tools',
    'website': "https://www.abcstrategie.it",
    'author': "ABC Strategie - Fabrizio D'Adamo",
    'license': "AGPL-3",
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/exercise_views.xml',
        'views/tutorial_views.xml',
        'views/menu.xml',
        'data/tutorial_data.xml',

    ],
    'demo': [],
}
