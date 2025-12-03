# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from odoo import models, fields

# Ajout du modèle Formation
class SchoolFormation(models.Model):
    _name = 'school.formation'       # Nom technique de la table (school_formation)
    _description = 'Formation'

    name = fields.Char(string="Type de formation", required=True)
    
    # Lien vers le RP (On filtre pour ne pouvoir choisir QUE des RP)
    rp_id = fields.Many2one('res.partner', string="Responsable Pédagogique", domain=[('is_rp', '=', True)])

    # Note : 
    # - id est automatique
    # - create_date est automatique
    # - write_date est automatique

# Extension du modèle res.partner pour ajouter le marqueur RP
class ResPartner(models.Model):
    _inherit = 'res.partner' # On modifie le contact standard

    # Notre marqueur pour identifier les RP
    is_rp = fields.Boolean(string="Est un RP", default=False)