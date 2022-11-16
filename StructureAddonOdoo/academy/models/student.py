from odoo import models, fields

class Student(models.Model):
    _name = 'student'
    _description = 'student'
    
    name = fields.Char(required=True)
    student_line_ids = fields.One2many('student.line', 'student_id')
    code = fields.Char()
    #course_id = fields.Many2one('course', related='course_line_ids.course_id')
    course_id = fields.Many2many('course')
    course_purchase_id = fields.Many2many('academy.purchase')
    course_line_ids = fields.One2many('course.line', 'course_id')
    
    #Asignaturas
    subject_id = fields.Char()

    subject_date = fields.Date()
    teacher_id = fields.Many2many('teacher')
    teacher_line_ids = fields.One2many('teacher.line', 'teacher_id')
    date_birth = fields.Date()
    email = fields.Char()
    address = fields.Char()
    movil = fields.Char()
    nif = fields.Char()
    create_date = fields.Date()
    end_date = fields.Date()
    #titulaciones


    notes = fields.Text()

class StudentLine(models.Model):
    _name = 'student.line'
    _description = 'student.line'

    name = fields.Char()
    course_id = fields.Many2one('course')
    student_id = fields.Many2one('student')
    teacher_id = fields.Many2one('teacher')



    




    