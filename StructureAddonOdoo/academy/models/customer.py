from odoo import models, fields

class Customer(models.Model):
    _name = 'customer'
    _description = 'customer'
    
    name = fields.Char(required=True)
    code = fields.Char()

    email = fields.Char()
    address = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Char()
    movil = fields.Char()
    student_id = fields.Many2many('student')
