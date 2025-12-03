{
    'name': "Gestion RP",
    'summary': "Gestion des Responsables Pédagogiques",
    'author': "MoonDev",
    'version': '1.0',
    'depends': ['base'], # On a besoin du module de base (Contacts)
    'data': [
        'views/views.xml', # On charge le fichier d'interface
    ],
    'installable': True,
    'application': True,
}