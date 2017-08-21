# -*- coding: utf-8 -*-
from odoo import http

# class Mettric(http.Controller):
#     @http.route('/mettric/mettric/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mettric/mettric/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mettric.listing', {
#             'root': '/mettric/mettric',
#             'objects': http.request.env['mettric.mettric'].search([]),
#         })

#     @http.route('/mettric/mettric/objects/<model("mettric.mettric"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mettric.object', {
#             'object': obj
#         })