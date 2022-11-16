from odoo import models, fields

class Subject(models.Model):
    _name = 'subject'
    _description = 'subject'
    
    name = fields.Char(required=True)
    code = fields.Char()
    course_id = fields.Many2many('course')
    teacher_id = fields.Many2many('teacher')
    student_id = fields.Many2many('student')
    exam_id = fields.Many2one('exam')
    