# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import datetime
from odoo.exceptions import UserError, Warning

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def button_validate(self):
        result = super(StockPicking, self).button_validate()
        
# Create invoice automatically
        for picking in self:
            if picking.picking_type_code == 'outgoing':
                
                so = self.env['sale.order'].search([('name','=',picking.origin)])
              
                if so.invoice_count == 0:

                    sale_adv =self.env['sale.advance.payment.inv'].create({'advance_payment_method':'all'})  

                    invoice = sale_adv.with_context(active_ids=so.ids).create_invoices()
                    invoice = so.invoice_ids

                    invoice.action_invoice_open()

 
                    template = self.env.ref('account.email_template_edi_invoice', False)
                    ctx = dict(
                        default_model='account.invoice',
                        default_res_id=invoice.id,
                        default_use_template=bool(template),
                        default_template_id=template and template.id or False,
                        default_composition_mode='comment',
                        mark_invoice_as_sent=True,
                        custom_layout="mail.mail_notification_paynow",
                        force_email=True,
                        active_ids=invoice.ids,
                    )
                             
                    invoice_send=self.env['account.invoice.send'].with_context(ctx).create({ })


                    invoice_send.onchange_template_id()
                    invoice_send._send_email()


# Print the correct label        
                if not result:
                    if picking.carrier_id.label_to_print =='carrier':
                        attachment = self.env['ir.attachment'].search([('res_model','=','stock.picking'),('res_id','=',picking.id),('name','=like','Label%')])
                        action = {
                            'name': attachment.name,
                            'type': 'ir.actions.act_url',
                            'url': "web/content/"+ str(attachment.id) + "?download=true",
                            'target': 'self',
                            }
                        return action
                    elif picking.carrier_id.label_to_print =='delivery_slip':
                        return self.env.ref('stock.action_report_delivery').with_context(discard_logo_check=True).report_action(self)
                else:
                    return result




