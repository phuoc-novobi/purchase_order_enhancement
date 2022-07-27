from tokenize import group
from odoo import api, models, fields
from odoo.exceptions import UserError


class ArchivePurchaseOrder(models.TransientModel):
    _name = 'archive.purchase.order'
    _description = 'Archive Multiple PO'

    archive_purchase_order_ids = fields.Many2many(
        'purchase.order',
        string="Purchase Orders"
    )
    button_archive_invisible = fields.Boolean(
        compute="_compute_button_invisible")

    @api.depends('archive_purchase_order_ids')
    def _compute_button_invisible(self):
        self.button_archive_invisible = False if len(
            self.archive_purchase_order_ids) > 0 else True

    def action_archive(self):
        self.archive_purchase_order_ids._check_accessability()
