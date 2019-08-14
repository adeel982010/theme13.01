# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    @api.model
    def _cron_check_batch_status(self):

        batch_in_progress = self.env['stock.picking.batch'].search([('state','=','in_progress')])
        for b in batch_in_progress:

            for p in b.picking_ids:
                if p.state not in ('done','cancel'):
                    p.write({'batch_id': None})
            
            # if pick_done:
            b.done()

