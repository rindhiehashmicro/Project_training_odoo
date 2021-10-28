# -*- coding: utf-8 -*-
 
from odoo import models, fields, api
 
class rindhiecounter(models.Model):
    _name = 'rindhiecounter.kategori'
    _description = 'Daftar Kategori Handphone'
    
    warna = fields.Char(string='Colour HP', required=True) 
    kondisi = fields.Selection(string='Kondisi Handphone',
                            selection=[('new', 'New'), ('second', 'Second')],
                            required=True
    )

    harga = fields.Integer(string='Harga Hp', required=True)
    
    tersedia = fields.Boolean(string='tersedia',
                             default=True
    )

    stock = fields.Integer(string='Stock Hp', required=True)

    stock_id = fields.Many2one(
    comodel_name='rindhiecounter.handphone', 
    string='Hp', 
    required=True,
    delegate=True)

    pegawai_id = fields.Many2one(comodel_name="res.partner", string="Penanggung Jawab", 
    domain="[('is_pegawainya','ilike',True)]")

    # qty = fields.Integer(compute='_compute_qty', string='qty')
    # kurangistock = fields.Many2many('rindhiecounter.detailpembelian', string = 'stock berkurang')

    @api.depends('stock_id')
    def _compute_deskrip(self):
        for record in self:
            record.deskrip = record.stock_id.deskripsi

    # @api.depends('stock', 'kurangistock')
    # def _compute_qty(self):
    #    for record in self:
    #         record.stock = record.stock - record.qty 
