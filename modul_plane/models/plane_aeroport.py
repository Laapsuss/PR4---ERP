from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    name = fields.Char(compute = '_get_name', string='name', readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('nom')
    imatge = fields.Char('Imatge')
    ciutat = fields.Char('ciutat')
    pais = fields.Char('pais')
    latitud = fields.Float('latitud')
    longitud = fields.Float('longitud')
    
    def _get_name(self):
        for record in self:
            record.name = str(record.name)