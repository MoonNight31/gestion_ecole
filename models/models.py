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

    # Extension du modèle res.partner pour gérer les groupes d'entreprises
    is_group = fields.Boolean(string="Est un Groupe d'entreprises")
    siren = fields.Char(string="SIREN")
    siege_social = fields.Char(string="Siège Social") # Note: Odoo a déjà street/city, mais on garde le vôtre si vous y tenez

    # --- LOGIQUE DU SMART BUTTON ---
    # Ce champ va compter combien d'entreprises sont rattachées à ce groupe
    subsidiary_count = fields.Integer(string="Nombre de filiales", compute='_compute_subsidiary_count')

    def _compute_subsidiary_count(self):
        for record in self:
            # On compte les contacts qui ont ce groupe comme parent (parent_id)
            # et qui sont des sociétés (is_company=True)
            record.subsidiary_count = self.env['res.partner'].search_count([
                ('parent_id', '=', record.id),
                ('is_company', '=', True)
            ])

    # Fonction qui se lance quand on clique sur le bouton "Filiales"
    def action_view_subsidiaries(self):
        self.ensure_one()
        return {
            'name': 'Filiales du Groupe',
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            # On filtre pour ne montrer que les enfants de ce groupe
            'domain': [('parent_id', '=', self.id), ('is_company', '=', True)],
            # Quand on crée une filiale depuis cette vue, elle est automatiquement rattachée au groupe
            'context': {'default_parent_id': self.id, 'default_is_company': True}
        }