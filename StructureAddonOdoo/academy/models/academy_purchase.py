from odoo import models, fields

class AcademyPurchase(models.Model):
    _name = 'academy.purchase'
    _description = 'academy.purchase'
    
    name = fields.Char()
    code = fields.Char()
    #facturas
    customer_id = fields.Many2one('student')
    create_date = fields.Date()
    end_date = fields.Date()
    #impuestos
    price_subtotal = fields.Integer()
    #estado de pago