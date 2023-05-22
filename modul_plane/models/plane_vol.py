from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    name = fields.Char(compute = '_get_name', string='name', readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    passatgers = fields.Char('passatgers')
    dataSortida = fields.Datetime('Data de Sortida')
    dataEntrada = fields.Datetime('Data de d''Entrada')
    
    def _get_name(self):
        for record in self:
            record.name = str(record.name)
    