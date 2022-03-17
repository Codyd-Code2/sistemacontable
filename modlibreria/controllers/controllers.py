# -*- coding: utf-8 -*-
from odoo import http
from sklearn import datasets

class Modlibreria(http.Controller):
    @http.route('/modlibreria/modlibreria', auth='public')
    def index(self, **kw):
        datasets.load_iris()
        digits = datasets.load_digits()
        print(digits.data)
        return "Hello instalar librerias"

#     @http.route('/modlibreria/modlibreria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modlibreria.listing', {
#             'root': '/modlibreria/modlibreria',
#             'objects': http.request.env['modlibreria.modlibreria'].search([]),
#         })

#     @http.route('/modlibreria/modlibreria/objects/<model("modlibreria.modlibreria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modlibreria.object', {
#             'object': obj
#         })
