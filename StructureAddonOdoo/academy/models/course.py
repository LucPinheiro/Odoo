from attr import field
from odoo import models, fields, api

class Course(models.Model):
    _name = 'course'
    _description = 'course'
    
    name = fields.Char(required=True, default="C")
    code = fields.Char()
    description = fields.Char()
    price_unit = fields.Float()
    product_id = fields.Many2one('course')
    tax_id = fields.Float(required=True, defaout= 23, compute='_compute_tax_id')
    price_tax = fields.Float(compute='_compute_price_tax')
    price_subtotal = fields.Float(string='Total', compute='_compute_subtotal_all')
    course_line_ids = fields.One2many('course.line', 'course_id')
    subject_id = fields.Many2many('subject')
    subject_qty = fields.Integer()
    study_guides = fields.Many2one('study.guides')
    #carga horaria
    
    student_id = fields.Many2many('student')
    student_id_count = fields.Integer('student', compute='_compute_student_count', String='Student number')
    student_line_ids = fields.One2many('student.line', 'student_id')
    teacher_id = fields.Many2many('teacher')
    teacher_line_ids = fields.One2many('teacher.line', 'teacher_id')
    teacher_id_count = fields.Integer()
    sale_id = fields.Many2one('academy_sale')
    create_date = fields.Date()
    end_date = fields.Date()
    category_id= fields.Char()

    notes = fields.Text()



    @api.depends()
    def _compute_name(self):
        for record in self:
            record.name = "C" + str(record.name)

    def _compute_student_count(self):
        for student in self:
            student.student_id_count = len(student.student_id) 


    def _compute_tax_id(self):
        for record in self: 
            record.tax_id = 23

    @api.depends('price_unit')
    def _compute_price_tax(self):
        for record in self:
            record.price_tax = (record.tax_id * record.price_unit) /100
    
    @api.depends('price_unit','tax_id')
    def _compute_subtotal_all(self):
        for record in self:
            record.update({
                'price_subtotal': record.price_unit + record.price_tax
            })


class CourseLine(models.Model):
    _name = 'course.line'
    _description = 'course.line'
    
    name = fields.Char()
    course_id = fields.Many2one('course')
    student_line_ids = fields.Many2one('student')
    teacher_line_ids = fields.Many2one('teacher')
    
