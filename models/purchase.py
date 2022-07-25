from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean('Is Active?', default=True)
    us_phone_number = fields.Char('US Phone Number')

    @api.model
    def _check_archivability(self):
        return len(self.filtered(lambda record: record.state not in ['done', 'cancel'])) > 0

    def action_archive(self):
        if not self.env.user.user_has_groups('purchase.group_purchase_manager'):
            raise UserError(
                'Only Administrators are allowed to archive records!')
        if self._check_archivability():
            raise UserError(
                'You cannot archive Purchase Orders that are not done/cancelled!')
        self.write({'active': False})

    def _schedule_archive(self):
        today = fields.Datetime.today()
        lifespan = self.env.company.lifespan
        expire_date = today - timedelta(days=lifespan)
        old_orders = self.env['purchase.order'].search(
            [('write_date', '<', expire_date), ('state', 'in', ['done', 'cancel'])])
        old_orders.write({'active': False})
