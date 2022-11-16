from odoo import models, fields

class Employee(models.Model):
    _name = 'employee'
    _description = 'employee'
    
    name = fields.Char(required=True)
    code = fields.Char()
    departments = fields.Char()

    teacher_id = fields.Many2many('teacher')
  
