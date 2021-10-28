# -*- coding: utf-8 -*-
 
from odoo import models, fields, api
 
class Order(models.Model):
    _name = 'rindhiecounter.order'
    _description = 'Daftar Order'
    
    name = fields.Char(string="Kode Pembelian", required=True)
    pemesan_id = fields.Many2one(comodel_name='res.partner', string='Nama Customer', domain="[('is_customernya','ilike',True)]")
    tanggal_pesan = fields.Datetime(string='Tanggal Pembelian', default=fields.Datetime.now)
    detailhp_ids = fields.One2many('rindhiecounter.detailpembelian', 'order_id', string='Detail Pembelian')
    jumlah_pesanan = fields.Integer(compute='_compute_jumlah_pesanan', string='Jumlah Pesanan')
    total_harga = fields.Char(compute='_compute_total_harga', string='Total Tagihan')

    @api.model
    def _compute_total_harga(self):
        for record in self:
            total = sum(self.env['rindhiecounter.detailpembelian'].search([('order_id','=',record.id)]).mapped('jumlah_harga'))
            record.total_harga = total
   
    @api.depends('detailhp_ids')
    def _compute_jumlah_pesanan(self):
        for record in self:
            record.jumlah_pesanan = len(record.detailhp_ids)

class detailPembelian(models.Model):
    _name = 'rindhiecounter.detailpembelian'
    _description = 'Detail Pembelian Hp'
 
    name = fields.Char(string='Kode Pembelian')
    order_id = fields.Many2one('rindhiecounter.order', string='Pembelian')
    stock_id = fields.Many2one('rindhiecounter.kategori', string='Handphone')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    qty = fields.Integer(string='Qty (pcs)')
    jumlah_harga = fields.Integer(compute='_compute_jumlah_harga', string='Jumlah Harga')
    
   
    @api.depends('qty')
    def _compute_jumlah_harga(self):
        for record in self:
            record.jumlah_harga = record.harga * record.qty

    @api.onchange('qty')
    def _onchange_qty(self):
        for record in self:
            record.stock_id.stock -= record.qty

   
    @api.depends('stock_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.stock_id.harga

