# -*- coding: utf-8 -*-
# from odoo import http


# class Ghozi-academy(http.Controller):
#     @http.route('/ghozi-academy/ghozi-academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ghozi-academy/ghozi-academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ghozi-academy.listing', {
#             'root': '/ghozi-academy/ghozi-academy',
#             'objects': http.request.env['ghozi-academy.ghozi-academy'].search([]),
#         })

#     @http.route('/ghozi-academy/ghozi-academy/objects/<model("ghozi-academy.ghozi-academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ghozi-academy.object', {
#             'object': obj
#         })
