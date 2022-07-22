from odoo import http
from odoo.http import request


class ArchiveController(http.Controller):
    @http.route('/purchase_order_enhancement/archive', type='json',
                auth='none')
    def action_archive(self, **params):
        def return_message(order_ids, code, message):
            return {
                "id": None,
                "result": {
                    "archived_orders": order_ids,
                    "code": code,
                    "message": message
                },
                "jsonrpc": "2.0"
            }
        if params['method'] != 'archive':
            return return_message(False, 400, f'Not supported method "{params["method"]}"')

        try:
            request.env['purchase.order'].sudo().browse(
                params['orders']).action_archive()
            return return_message(params['orders'], 200, 'Successful')
        except:
            return return_message(False, 400, "Order not found / Order not locked or cancelled")
