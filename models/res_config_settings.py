from email.policy import default
from odoo import models, fields


class ConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_archive_purchase = fields.Boolean(
        "Archive Cancelled/Locked Purchase Orders",
        default=False,
        implied_group='purchase_order_enhancement.group_archive_purchase'
    )
