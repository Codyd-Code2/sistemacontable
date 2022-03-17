# -*- coding: utf-8 -*-

from odoo import models, fields, api
from sklearn import datasets
from sklearn.externals import joblib

class modlibreria(models.Model):
    _name = 'modlibreria.modlibreria'
    _description = 'modlibreria.modlibreria'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Integer(compute="_value_pc", store=True)
    value3 = fields.Float(compute="predecir",store=True)

    @api.depends('value')
    def predecir(self):
        clf=joblib.load('modelo_entrenado.pkl')
        iris=datasets.load_iris()
        result=clf.score(iris.data, iris.target)
        for record in self:
            record.value3 = result * 100



    @api.depends('value')
    def _value_pc(self):
        datasets.load_iris()
        digits = datasets.load_digits()
        dato=digits.data.argmax()

        for record in self:
            record.value2 = record.value + dato
