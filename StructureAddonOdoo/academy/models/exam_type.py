from odoo import models, fields

class Exam(models.Model):
    _name = 'exam'
    _description = 'exam'
    
    name = fields.Char(required=True)
    code = fields.Char()
    exam_type = fields.Integer()
    course_id = fields.Many2many('course')
    teacher_id = fields.Many2many('teacher')
    student_id = fields.Many2many('student')
    start_date = fields.Date()
    end_date = fields.Date()