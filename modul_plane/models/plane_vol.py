from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    name = fields.Char(compute = '_get_name', string='name', readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    passatgers = fields.Char('passatgers')
    dataSortida = fields.Datetime('Data de Sortida')
    dataEntrada = fields.Datetime('Data de d''Entrada')
    desti_id = fields.Many2one('plane.aeroport', 'vol_ids', string='Desti')
    origen_id = fields.Many2one('plane.aeroport', string='Origen')
    avio_id = fields.Many2one('plane.avio', string="Avio")
    pilot_id = fields.Many2one('plane.pilot', string="Pilot")

    
    def _get_name(self):
        for record in self:
            record.name = str(record.name)
    