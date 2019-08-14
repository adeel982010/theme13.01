# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class sale_order(models.Model):

    _inherit = "sale.order"

    @api.constrains('state')
    def _check_state_change(self):
        for rec in self:
            if rec.state == 'done' or rec.state == 'sale':
                livraison_product = False
                
                for line in rec.order_line:
                    if line.product_id.categ_id.livraison:
                        livraison_product = True
                
                if livraison_product == False : 
                    raise UserError ('Vous devez ajouter au moins un produit livraison pour confirmer le devis.')