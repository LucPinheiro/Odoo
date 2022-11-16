from odoo import models, fields

class Teacher(models.Model):
    _name = 'teacher'
    _description = 'teacher'
    
    name = fields.Char(required=True)
    code = fields.Char()
    course_id = fields.Many2many('course')
    course_line_ids = fields.Many2one('course.line')
    teacher_line_ids = fields.One2many('teacher.line', 'teacher_id')
    student_id = fields.Many2many('student')
    category_id = fields.Char()
    date_birth = fields.Date()
    email = fields.Char()
    address = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Char()
    movil = fields.Char()
    nif = fields.Char()


    notes = fields.Text()


class TeacherLine(models.Model):
    _name = 'teacher.line'
    _description = 'teacher.line'

    name = fields.Char()
    teacher_id = fields.Many2one('teacher') 



