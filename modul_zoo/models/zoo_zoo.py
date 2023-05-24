from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    name = fields.Char(compute = '_get_name', string='name', readonly='True', store=False)
    id = fields.Integer('Id', required=True)
    grandaria = fields.Float('grandaria')
    nom = fields.Char('nom')
    ciutat = fields.Char('ciutat')
    pais = fields.Char('pais')
    animal_ids = fields.one2Many('zoo.animal', 'zoo_id', string="Animals")

    def _get_name(self):
        for record in self:
            record.name = str(record.name)