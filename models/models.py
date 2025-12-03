# -*- coding: utf-8 -*-

from odoo import models, fields, api

# ========== RESPONSABLE PÉDAGOGIQUE (RP) ==========
class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Marqueur pour identifier les RP
    is_rp = fields.Boolean(string="Est un RP", default=False)
    
    # Relations inverses
    formation_ids = fields.One2many('school.formation', 'rp_id', string="Formations gérées")
    formation_count = fields.Integer(string="Nombre de formations", compute='_compute_formation_count')

    @api.depends('formation_ids')
    def _compute_formation_count(self):
        for record in self:
            record.formation_count = len(record.formation_ids)


# ========== FORMATION ==========
class SchoolFormation(models.Model):
    _name = 'school.formation'
    _description = 'Formation'
    _rec_name = 'type_formation'

    type_formation = fields.Char(string="Type de formation", required=True)
    rp_id = fields.Many2one('res.partner', string="Responsable Pédagogique", 
                            domain=[('is_rp', '=', True)], required=True)
    
    # Relations inverses
    personne_ids = fields.One2many('school.personne', 'formation_id', string="Étudiants")
    etudiant_count = fields.Integer(string="Nombre d'étudiants", compute='_compute_etudiant_count')

    @api.depends('personne_ids')
    def _compute_etudiant_count(self):
        for record in self:
            record.etudiant_count = len(record.personne_ids.filtered(lambda p: p.type_profil == 'etudiant'))


# ========== PERSONNE (Étudiant, Alumni, Intervenant, Salarié) ==========
class SchoolPersonne(models.Model):
    _name = 'school.personne'
    _description = 'Personne (Étudiant, Alumni, Intervenant, Salarié)'
    _rec_name = 'display_name'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    display_name = fields.Char(string="Nom complet", compute='_compute_display_name', store=True)
    email = fields.Char(string="Email")
    adresse = fields.Text(string="Adresse")
    telephone = fields.Char(string="Téléphone")
    
    # Marqueurs de profil
    is_alumni = fields.Boolean(string="Est un Alumni", default=False)
    type_profil = fields.Selection([
        ('etudiant', 'Étudiant'),
        ('alumni', 'Alumni'),
        ('intervenant', 'Intervenant'),
        ('salarie', 'Salarié'),
    ], string="Type de profil", required=True, default='etudiant')
    
    poste = fields.Char(string="Poste")
    is_intervenant = fields.Boolean(string="Est intervenant", default=False)
    
    # Relations
    formation_id = fields.Many2one('school.formation', string="Formation",
                                   ondelete='set null', 
                                   help="Formation suivie (pour les étudiants)")

    @api.depends('nom', 'prenom')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.prenom} {record.nom}"