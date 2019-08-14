# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, values):

        values['default_code'] = self.env['ir.sequence'].next_by_code('seq.product.reference')

        result = super(ProductTemplate, self).create(values)

        return result

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals):

        vals['default_code'] = self.env['ir.sequence'].next_by_code('seq.product.reference')

        res = super(ProductProduct, self).create(vals)

        return res
