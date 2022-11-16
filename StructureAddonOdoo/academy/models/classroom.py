from odoo import models, fields

class ClassRoom(models.Model):
    _name = 'classroom'
    _description = 'classroom'
    
    name = fields.Char(required=True)
    code = fields.Char()
    course_id = fields.Many2many('course')
    teacher_id = fields.Many2many('teacher')
    student_id = fields.Many2many('student')