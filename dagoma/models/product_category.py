# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import Warning

class ProductCategory(models.Model):
    _inherit = "product.category"

    livraison = fields.Boolean(default=False,string="Livraison")

    @api.multi
    def write(self,values):
        for rec in self:
            if 'livraison' in values and rec.livraison == True:

                sale_order= self.env['sale.order'].search(['|',('state','=','done'),('state','=','done')])
                sale_lines =self.env['sale.order.line'].search([('product_id.categ_id','=',rec.id),('order_id','in',sale_order.ids)])

                if sale_lines:
                    raise Warning(_("You cannot change the livraison state of a category already used"))
        return super(ProductCategory, self).write(values)