from odoo import api, fields, models, _


class DeliverCarrier(models.Model):
    _inherit = 'delivery.carrier'

    label_to_print=fields.Selection([('carrier','carrier'),('delivery_slip','delivery_slip')], string="Lable to print")

    picking_ready = fields.Integer(compute="_number_of_picking")

    @api.depends('name')
    def _number_of_picking(self):
        for rec in self:
            picking = self.env['stock.picking'].search([('state','=','assigned'),('carrier_id','=',rec.id),('picking_type_code','=','internal'),('batch_id','=',None)])
            rec.picking_ready = len(picking.ids)

    @api.multi
    def create_batch(self):
        for rec in self:
            number_of_batch = rec.picking_ready// 6

            picking = self.env['stock.picking'].search([('state','=','assigned'),('carrier_id','=',rec.id),('picking_type_code','=','internal'),('batch_id','=',None)])
            
            batch = self.env['stock.picking.batch'].create({'state' : 'draft',})

            for i in picking[0:6]:
                i.write({'batch_id':batch.id})

            batch.confirm_picking()
            return batch.print_picking()

   