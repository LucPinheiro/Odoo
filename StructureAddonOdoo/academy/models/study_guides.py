from odoo import models, fields

class StudyGuides(models.Model):
    _name = 'study.guides'
    _description = 'Study guides'
    
    name = fields.Char(required=True)
    code = fields.Char()
    course_id = fields.Many2many('course')
