{
    'name': "Gestion Ecole",
    'summary': "Gestion de l'école",
    'author': "MoonDev",
    'version': '1.0',
    'depends': ['base'], # On a besoin du module de base (Contacts)
    'data': [
        'security/ir.model.access.csv',  # <--- AJOUTEZ CETTE LIGNE EN PREMIER
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}