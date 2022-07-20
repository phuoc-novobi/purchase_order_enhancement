from tokenize import group
from odoo import models, fields, api
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(
        'Is Active?',
        default=True,
        readonly=True,
        states={'done': [('readonly', False)], 'cancel': [
            ('readonly', False)]},
        groups='purchase.group_purchase_manager'
    )

    def button_archive(self):
        if self.state in ['cancel', 'done']:
            self.write({'active': False})
        return {}

    def action_archive(self):
        if len(self.filtered(lambda record: record.state not in ['done', 'cancel'])) > 0:
            raise UserError(
                'You cannot archive Purchase Orders that are not done/cancelled!')
        for record in self.filtered(lambda record: record.state in ['done', 'cancel']):
            record.write({'active': False})
