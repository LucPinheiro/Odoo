from odoo import models, fields, api

class AcademySale(models.Model):
    _name = 'academy.sale'
    _description = 'academy.sale'
    
    #Venta al cliente
    name = fields.Char(string='Number')
    code = fields.Char()
    academy_sale_order_id = fields.Many2one('academy.sale')
    create_date = fields.Date()
    customer_id = fields.Many2one('student', string='Customer')
    product_id = fields.Many2many('course')
    product_qty = fields.Integer('course', compute='_compute_product_count')
    uom_id = fields.Integer()
    price_unit = fields.Float(related='product_id.price_unit',  compute='_compute_price_unit', string='Price', Store='True')
    #currency_id = fields.Many2one(related='price_unit.currency_id')
    tax_id = fields.Float(related='product_id.tax_id', compute='_compute_tax_id')
    price_tax = fields.Float(compute='_compute_price_tax')
    price_subtotal = fields.Float(string='Total', compute='_subtotal_all')
    
    amount_untaxed = fields.Float()
    amount_tax = fields.Float() 
    amount_total =  fields.Float(compute='_compute_amount_alls')


    state = fields.Selection([('notstarted', 'Quotation')])
    student_id = fields
    course_line_ids = fields.One2many('course.line', 'course_id')
    academy_sale_line_ids = fields.One2many('academy.sale.line', 'academy_sale_id')
    

    #Firma del Cliente
    signed_id = fields.Many2one('student')
    signed_on = fields.Date()
    signature = fields.Binary()

    #signature = fields.Image('Signature', help='Signature received through the portal.', copy=False, attachment=True, max_width=1024, max_height=1024)

    
    def _compute_name(self):
        for record in self:
            record.name = ""

    @api.depends('price_unit')
    def _compute_price_unit(self):
        for record in self:
            record.price_unit = (record.price_unit * record.product_qty)

    # # #@api.depends('product_id')
    # def _compute_price_unit(self):
    #      for price in self:
    #          price.update({
    #           'price_unit': sum(self.mapped('product_id'))
    #             })

    def _compute_product_count(self):
        for product in self:
            product.product_qty = len(product.product_id) 

    def _compute_price_tax(self):
        for record in self:
            record.price_tax = (record.tax_id * record.price_unit) /100
    
    @api.depends('price_unit','tax_id')
    def _subtotal_all(self):
        for record in self:
            record.update({
                'price_subtotal': record.price_unit + record.price_tax
            })



    #@api.depends('academy_sale_line_ids.price_total')
    def _compute_amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.academy_sale_line_ids:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax,
            })

    def _compute_amount_alls(self):
        for rec in self:
            total = 0
            for line in rec.academy_sale_line_ids:
                total += line.price_subtotal
                rec['amount_total'] = total

# saldo = fields.Float('Saldo',compute="_compute_saldo"

# def _compute_saldo(self):
#     for rec in self:
#         rec.saldo = sum(self.lineas.mappend('amount'))

    # def save_and_new_course(self):
    #     self.create_update_purchase_order_line()
    #     self.course_id = False
    #     self.product_id = False
    #     self.price = 0
    #     return self.env['purchase.order']._purchase_qr_code_reading_open_wizard(self.id)

    # def save_and_next_course(self):
    #     self.create_update_purchase_order_line()
    #     return self.env['purchase.order']._purchase_qr_code_reading_open_wizard(self.id)

    # def save_and_close_course(self):
    #     self.create_update_purchase_order_line()
    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'reload',
    #     }

    
    # def _create_payment_transaction(self, vals):

    #     vals.update({
    #             'total': sum(self.mapped('price_total'))
    #         })



class AcademySaleLine(models.Model):
    _name = 'academy.sale.line'
    _description = 'academy.sale.line'

    
    name = fields.Char()
    academy_sale_id = fields.Many2one('academy.sale')
    amount_tax = fields.Float()
    product_id = fields.Many2one('course')
    product_qty = fields.Integer()
    price_unit = fields.Float(related='product_id.price_unit')
    tax_id = fields.Float(related='product_id.tax_id')
    price_tax = fields.Float(related='product_id.price_tax', compute='_compute_price_tax')
    price_subtotal = fields.Float(string='Total', compute='_compute_subtotal_all')

  
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



