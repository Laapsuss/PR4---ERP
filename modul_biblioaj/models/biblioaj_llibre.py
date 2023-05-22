from odoo import models, fields     
class biblioaj_llibre(models.Model): 
    _name = 'biblioaj.llibre' 
    codi = fields.Char('Codi', required=True) 
    titol = fields.Char('Títol', required=True)     
    isbn = fields.Char('ISBN', required=True)     
    pagines = fields.Char('Nombre de pàgines')   
    isbn = fields.Text('Descripció')