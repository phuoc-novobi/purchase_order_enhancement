from odoo import http
from odoo.http import request


class ArchiveController(http.Controller):
    @http.route('/purchase_order_enhancement/archive', type='json',
                auth='none')
    def action_archive(self, **params):
        failed_result = {
            "id": None,
            "result": {
                "archived_orders": False,
                "code": 404,
                "message": "Could not found"
            },
            "jsonrpc": "2.0"
        }
        if params['method'] != 'archive':
            return failed_result

        try:
            request.env['purchase.order'].sudo().browse(
                params['orders']).action_archive()
            return {
                "id": None,
                "result": {
                    "archived_orders": params['orders'],
                    "code": 200,
                    "message": "Successful"
                },
                "jsonrpc": "2.0"
            }
        except:
            return failed_result
