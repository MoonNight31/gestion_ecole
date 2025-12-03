# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner' # On modifie le contact standard

    # Notre marqueur pour identifier les RP
    is_rp = fields.Boolean(string="Est un RP", default=False)