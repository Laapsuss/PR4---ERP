from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    name = fields.Char(compute = '_get_name', string='name', readonly='True', store=False)
    id = fields.Integer('Id', required=True)
    continentOrigen = fields.Char('Continent Origen')
    datanaix = fields.Date('Data de naixament')
    PaisOrigen = fields.Char('Pais Origen')
    sexe = fields.Char('Sexe')

    def _get_name(self):
        for record in self:
            record.name = str(record.name)