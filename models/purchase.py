from odoo import models, fields
from odoo.exceptions import UserError
from datetime import timedelta


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(
        'Is Active?',
        default=True,
        groups='purchase.group_purchase_manager'
    )
    us_phone_number = fields.Char('US Phone Number')

    def button_archive(self):
        if self.state in ['cancel', 'done']:
            self.write({'active': False})

    def action_archive(self):
        if len(self.filtered(lambda record: record.state not in ['done', 'cancel'])) > 0:
            raise UserError(
                'You cannot archive Purchase Orders that are not done/cancelled!')
        self.write({'active': False})

    def _schedule_archive(self):
        today = fields.Datetime.today()
        lifespan = self.env.company.lifespan
        expire_date = today - timedelta(days=lifespan)
        for record in self.env['purchase.order'].search([('write_date', '<', expire_date), ('state', 'in', ['done', 'cancel'])]):
            record.write({'active': False})
