from odoo import http

class TutorialController(http.Controller):
    @http.route('/tutorial', auth='public', website=True)
    def index(self, **kw):
        return "Benvenuti al Tutorial Odoo!"
