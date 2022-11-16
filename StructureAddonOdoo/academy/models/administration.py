from odoo import models, fields

class Administration(models.Model):
    _name = 'administration'
    _description = 'administration'
    
    name = fields.Char(required=True)
    code = fields.Char()
    departments = fields.Char()
    email = fields.Char()
    movil = fields.Char()


  
