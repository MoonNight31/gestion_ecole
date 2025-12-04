{
    'name': "Gestion École",
    'icon': '/gestion_ecole/static/description/icon.png',
    'web_icon': 'gestion_ecole/static/description/icon.png',
    'summary': "Gestion des formations, RP et étudiants",
    'description': """
        Module de gestion d'école
        ==========================
        * Responsables Pédagogiques (RP)
        * Formations
        * Étudiants et Personnes (Alumni, Intervenants, Salariés)
    """,
    'author': "MoonDev",
    'version': '1.0',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}