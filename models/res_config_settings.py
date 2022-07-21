from odoo import api, models, fields


class ConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    lifespan = fields.Integer(
        string='Lifespan',
        related='company_id.lifespan',
        readonly=False
    )
