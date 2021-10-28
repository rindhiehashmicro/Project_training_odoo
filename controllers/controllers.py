# -*- coding: utf-8 -*-
# from odoo import http

from odoo import http
from odoo.http import request
 
import json
 
 
class ModelDasar(http.Controller):
    @http.route('/jenishandphone', auth='public')
    def index(self, **kw):
        model = request.env['rindhiecounter.handphone'].search([])
        value = []
        for data in model:
            value.append({
                'nama':data.name,
                'ram':data.ram,
                'memory':data.memory,
                'type bahan':data.type
            })
        # value = [{
        #     'nama':'Rindhie Antika',
        #     'alamat':'Jakarta Selatan',
        #     'hobi':'Tidur'
        # }]
        return json.dumps(value)
   
    @http.route('/kategori', auth='public')
    def index1(self, **kw):
        model = request.env['rindhiecounter.kategori'].search([])
        value = []
        for data in model:
            value.append({
                'warna':data.warna,
                'harga per pcs':data.harga,
                'kondisi':data.kondisi
            })
        return json.dumps(value)



# class Rindhiecounter(http.Controller):
#     @http.route('/rindhiecounter/rindhiecounter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rindhiecounter/rindhiecounter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rindhiecounter.listing', {
#             'root': '/rindhiecounter/rindhiecounter',
#             'objects': http.request.env['rindhiecounter.rindhiecounter'].search([]),
#         })

#     @http.route('/rindhiecounter/rindhiecounter/objects/<model("rindhiecounter.rindhiecounter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rindhiecounter.object', {
#             'object': obj
#         })
