from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    name = fields.Char(compute = '_get_name', string='name', readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    imatge = fields.Char('Imatge')
    marca = fields.Integer('Marca')
    model = fields.Char('Model')
    maxVel = fields.Float('Velocitat Màxima')
    vol_ids = fields.one2Many('plane.vol', 'avio_id', string="Vols")
    
    def _get_name(self):
        for record in self:
            record.name = str(record.name)