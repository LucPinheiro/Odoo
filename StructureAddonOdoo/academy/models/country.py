from odoo import models, fields

class Country(models.Model):
    _name = 'country'
    _description = 'country'
    
    name = fields.Char(required=True)
    code = fields.Char()

    teacher_id = fields.Many2many('teacher')
    student_id = fields.Many2many('student')
