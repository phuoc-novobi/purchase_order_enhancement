from odoo import api, models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    lifespan = fields.Integer('Life Span', default=1)

    @api.constrains('lifespan')
    def _check_lifespan_negative(self):
        if self.lifespan < 0:
            raise models.ValidationError(
                'Lifespan must be a non-negative number')
