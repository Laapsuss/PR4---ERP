from odoo import models, fields

class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    name = fields.Char(compute='_get_name', string='Name', readonly=True, store=False)
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom')
    imatge = fields.Char('Imatge')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    latitud = fields.Float('Latitud')
    longitud = fields.Float('Longitud')

    @api.depends('nom')
    def _get_name(self):
        for record in self:
            record.name = str(record.nom)
