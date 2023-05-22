from odoo import models, fields
class biblioaj_autor(models.Model):
    _name = 'biblioaj.autor'
    nom = fields.Char('Nom', required=True)
    cognoms = fields.Char('Cognoms')
    datanaix = fields.Date('Data de naixament')
    telf = fields.Char('Telèfon')
    email = fields.Char('Correu electrònic')