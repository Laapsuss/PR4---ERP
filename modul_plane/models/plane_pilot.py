from odoo import models, fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    name = fields.Char(compute = '_get_name', string='name', readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom')
    cognoms = fields.Char('Cognoms')
    nif = fields.Char('Nif')
    pais = fields.Char('pais')
    telf = fields.Char('Telèfon')
    email = fields.Char('Correu electrònic')
    vol_ids = fields.one2Many('plane.vol', 'pilot_id', string="Vols")

    def _get_name(self):
        for record in self:
            record.name = str(record.name)