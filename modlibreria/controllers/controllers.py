# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Modlibreria(http.Controller):
    @http.route('/modlibreria/<model("modlibreria.modlibreria"):libro', auth='public')
    def index(self, libro):
        return http.request.render('modlibreria.libro' , {
            'libro': libro
        })

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
