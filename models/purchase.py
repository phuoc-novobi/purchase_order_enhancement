from odoo import api, models, fields
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(
        'Is Active?',
        default=True,
        readonly=True,
        states={'done': [('readonly', False)], 'cancel': [
            ('readonly', False)]},
        groups='purchase.group_purchase_manager, purchase_order_enhancement.group_archive_purchase'
    )

    def button_archive(self):
        if self.state in ['cancel', 'done']:
            self.write({'active': False})
        return {}

    def action_archive(self):
        if len(self.filtered(lambda record: record.state not in ['done', 'cancel'])) > 0:
            raise UserError(
                'You cannot archive Purchase Orders that are not done/cancelled!')
        for record in self:
            record.write({'active': False})


class ArchivePurchaseOrder(models.TransientModel):
    _name = 'archive.purchase.order'
    _description = 'Archive Multiple PO'

    archive_purchase_order_ids = fields.Many2many(
        'purchase.order', string="Purchase Orders")
    button_archive_invisible = fields.Boolean(
        compute="_compute_button_invisible")

    @api.depends('archive_purchase_order_ids')
    def _compute_button_invisible(self):
        self.button_archive_invisible = False if len(
            self.archive_purchase_order_ids) > 0 else True

    def action_archive(self):
        if len(self.archive_purchase_order_ids.filtered(lambda record: record.state not in ['done', 'cancel'])) > 0:
            raise UserError(
                'You cannot archive Purchase Orders that are not done/cancelled!')
        for record in self.archive_purchase_order_ids:
            record.write({'active': False})
