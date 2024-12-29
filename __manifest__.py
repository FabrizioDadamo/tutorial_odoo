{
    'name': "Apprendimento Odoo",
    'version': "1.0",
    'summary': "Modulo per apprendere l'utilizzo di Odoo attraverso tutorial ed esercizi guidati",
    'sequence': -100,
    'description': """Modulo interattivo per guidare i nuovi sviluppatori di Odoo ...""",
    'category': 'Tools',
    'website': "https://www.abcstrategie.it",
    'author': "ABC Strategie - Fabrizio D'Adamo",
    'license': "AGPL-3",
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': ['base'],
    'data': [
        # 1) regole sicurezza
        'security/ir.model.access.csv',
        # 2) menu e azioni
        'views/menu.xml',
        # 3) viste e form di tutorial
        'views/exercise_views.xml',
        'views/tutorial_views.xml',
        # 4) dati di esempio
        'data/tutorial_data.xml',
    ],
    'demo': [],
}
