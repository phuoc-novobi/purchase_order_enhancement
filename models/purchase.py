from odoo import api, models, fields
from odoo.exceptions import UserError
from datetime import timedelta


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

    def action_archive(self):
        if len(self.filtered(lambda record: record.state not in ['done', 'cancel'])) > 0:
            raise UserError(
                'You cannot archive Purchase Orders that are not done/cancelled!')
        self.write({'active': False})

    def _schedule_archive(self):
        today = fields.Datetime.today()
        lifespan = self.env.company.lifespan
        for record in self.env['purchase.order'].search([]).filtered(lambda r: r.write_date + timedelta(days=lifespan) < today and r.state in ['done', 'cancel']):
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
