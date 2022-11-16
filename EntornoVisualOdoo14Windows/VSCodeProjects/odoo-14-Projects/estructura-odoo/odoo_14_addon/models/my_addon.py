from odoo import models, fields

class MyAddon(models.Model):
    _name = 'my.addon'
    _description = 'my.addon'
    
    name = fields.Char()
    