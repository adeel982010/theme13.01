from odoo import api, fields, models, _


class DeliverCarrier(models.Model):
    _inherit = 'delivery.carrier'

    label_to_print=fields.Selection([('carrier','carrier'),('delivery_slip','delivery_slip')], string="Lable to print")

    picking_ready = fields.Integer(compute="_number_of_picking")

    @api.depends('name')
    def _number_of_picking(self):
        for rec in self:
            picking = self.env['stock.picking'].search([('state','=','assigned'),('carrier_id','=',rec.id),('picking_type_code','=','outgoing'),('batch_id','=',None)])
            rec.picking_ready = len(picking.ids)

    @api.multi
    def create_batch(self):
        for rec in self:
            number_of_batch = rec.picking_ready// 6
            # import ipdb; ipdb.set_trace()

            picking = self.env['stock.picking'].search([('state','=','assigned'),('carrier_id','=',rec.id),('picking_type_code','=','outgoing'),('batch_id','=',None)])

            # for i in range(0,number_of_batch):
            #     import ipdb; ipdb.set_trace()
            #     batch = self.env['stock.picking.batch'].create({ 'state' : 'draft', })

            #     picking_to_process = picking[0:6]
            #     import ipdb; ipdb.set_trace()
            #     for j in picking_to_process:
            #         import ipdb; ipdb.set_trace()
            #         j.write({'batch_id':batch.id})

            #     picking = picking[6:len(picking)]
            #     import ipdb; ipdb.set_trace()
            #     batch.confirm_picking()
            
            # import ipdb; ipdb.set_trace()
            # batch = self.env['stock.picking.batch'].create({'state' : 'draft',})

            # for j in picking:
            #     import ipdb; ipdb.set_trace()
            #     j.write({'batch_id':batch.id})

            # batch.confirm_picking()
            
            batch = self.env['stock.picking.batch'].create({'state' : 'draft',})

            for i in picking[0:6]:
                i.write({'batch_id':batch.id})

            batch.confirm_picking()
            return batch.print_picking()

   