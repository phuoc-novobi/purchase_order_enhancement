from odoo import http
from odoo.exceptions import UserError
from odoo.http import request


class ArchiveController(http.Controller):
    @http.route('/purchase_order_enhancement/archive', type='json',
                auth='public')
    def action_archive(self, **params):
        def return_result(order_ids, code, message):
            return {
                "archived_orders": order_ids,
                "code": code,
                "message": message
            }
        if 'method' not in params.keys() or 'orders' not in params.keys():
            return return_result(False, 404, f'Could not find your request!')
        if params['method'] != 'archive':
            return return_result(False, 400, """Not supported method '{}'""".format(params["method"]))
        archive_ids = request.env['purchase.order'].sudo().browse(
            params['orders'])
        try:
            archive_ids.action_archive()
            return return_result(params['orders'], 200, 'Successful')
        except UserError as e:
            if len(archive_ids.exists()) == len(archive_ids):
                return return_result(False, 400, str(e))
            return return_result(False, 400, 'Purchase Order ID not found')
