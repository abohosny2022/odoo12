# -*- coding: utf-8 -*-
from odoo import http

# class Override(http.Controller):
#     @http.route('/override/override/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/override/override/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('override.listing', {
#             'root': '/override/override',
#             'objects': http.request.env['override.override'].search([]),
#         })

#     @http.route('/override/override/objects/<model("override.override"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('override.object', {
#             'object': obj
#         })