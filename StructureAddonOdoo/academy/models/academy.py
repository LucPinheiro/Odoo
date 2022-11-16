from odoo import models, fields

class Academy(models.Model):
    _name = 'academy'
    _description = 'academy'
    
    name = fields.Char()
    code= fields.Char()
    course_id = fields.Many2one('course')
    student_id = fields.Many2one('student')
    teacher_id = fields.Many2one('teacher')
    employee_id = fields.Char()
    #CentroAcademia
    email = fields.Char()
    address = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Char()
    movil = fields.Char()