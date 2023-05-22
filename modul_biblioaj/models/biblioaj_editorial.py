from odoo import models, fields     
class biblioaj_editorial(models.Model): 
    _name = 'biblioaj.editorial' 
    nom = fields.Char('Nom', required=True) 
    adreca = fields.Char('Adreça')     
    telf = fields.Char('Telèfon')     
    email = fields.Char('Correu electrònic')