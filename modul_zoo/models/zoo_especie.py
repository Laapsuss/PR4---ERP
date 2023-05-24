from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    name = fields.Char(compute = '_get_name', string='name', readonly='True', store=False)
    id = fields.Integer('Id', required=True)
    familia = fields.Char('Familia')
    nomCientific = fields.Char('Nom Cientific')
    nomVulgar = fields.Char('Nom Vulgar')
    perill = fields.Boolean('perill')
    animals_ids = fields.one2Many('zoo.animal', 'especie_id', string="Animals")

    def _get_name(self):
        for record in self:
            record.name = str(record.name)