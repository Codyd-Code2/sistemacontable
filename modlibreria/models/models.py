# -*- coding: utf-8 -*-

from odoo import models, fields, api
from sklearn import datasets

class modlibreria(models.Model):
    _name = 'modlibreria.modlibreria'
    _description = 'modlibreria.modlibreria'

#     name = fields.Char()
#     value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)

    def _value_pc(self):
         datasets.load_iris()
         digits = datasets.load_digits()
         dato = digits.data
         for record in self:
             record.value2 = dato[0]
