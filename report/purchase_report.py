
from odoo import api, fields, models


class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    payment_term_id = fields.Many2one('account.payment.term', 'Payment Terms',
                                      domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    def _select(self):
        return super(PurchaseReport, self)._select() + ', po.payment_term_id as payment_term_id'

    def _group_by(self):
        return super(PurchaseReport, self)._group_by() + ', po.payment_term_id'
