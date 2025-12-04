# -*- coding: utf-8 -*-

from odoo import models, fields, api

# ========== EXTENSION DE RES.PARTNER (pour tous les contacts) ==========
class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Marqueur pour identifier les RP
    is_rp = fields.Boolean(string="Est un RP", default=False)
    
    # Type de personne (pour les particuliers)
    type_personne = fields.Selection([
        ('etudiant', 'Étudiant'),
        ('alumni', 'Alumni'),
        ('intervenant', 'Intervenant'),
        ('salarie', 'Salarié'),
        ('rp', 'Responsable Pédagogique'),
    ], string="Type de personne")
    
    # Champs spécifiques école
    is_alumni = fields.Boolean(string="Est un Alumni", default=False)
    is_intervenant = fields.Boolean(string="Est intervenant", default=False)
    poste = fields.Char(string="Poste")
    
    # Relations
    formation_id = fields.Many2one('school.formation', string="Formation",
                                   ondelete='set null', 
                                   help="Formation suivie (pour les étudiants)")
    
    # Relations inverses (pour les RP)
    formation_rp_ids = fields.One2many('school.formation', 'rp_id', string="Formations gérées")
    formation_count = fields.Integer(string="Nombre de formations", compute='_compute_formation_count')

    @api.depends('formation_rp_ids')
    def _compute_formation_count(self):
        for record in self:
            record.formation_count = len(record.formation_rp_ids)

    @api.onchange('is_rp')
    def _onchange_is_rp(self):
        if self.is_rp:
            self.type_personne = 'rp'
            self.is_company = False


# ========== FORMATION ==========
class SchoolFormation(models.Model):
    _name = 'school.formation'
    _description = 'Formation'
    _rec_name = 'type_formation'

    type_formation = fields.Char(string="Type de formation", required=True)
    rp_id = fields.Many2one('res.partner', string="Responsable Pédagogique", 
                            domain=[('is_rp', '=', True), ('is_company', '=', False)], 
                            required=True)
    
    # Relations inverses
    etudiant_ids = fields.One2many('res.partner', 'formation_id', string="Étudiants",
                                   domain=[('type_personne', '=', 'etudiant')])
    etudiant_count = fields.Integer(string="Nombre d'étudiants", compute='_compute_etudiant_count')

    @api.depends('etudiant_ids')
    def _compute_etudiant_count(self):
        for record in self:
            record.etudiant_count = len(record.etudiant_ids)