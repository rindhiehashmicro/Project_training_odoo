# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ModelDasar(models.Model):
    _name = 'rindhiecounter.base'
    _description = 'model dasar rindhie counter'
 
    ram = fields.Selection(string="RAM", selection=[('4gb', '4GB'), ('6gb', '6GB'), ('8gb', '8GB')])
    memory = fields.Selection(string="Memory", selection=[('64gb', '64GB'), ('128gb','128GB'),
    ('512gb','512GB')])
    type = fields.Selection(string='Type Handphone', selection=[('iphone','Iphone'),('android','Android')])


class rindhiecounter(models.Model):
    _name = 'rindhiecounter.handphone'
    _description = 'Daftar Jenis Handphone'
    _inherit = "rindhiecounter.base"

    name = fields.Char(string='Merk & Seri Hp', required=True)
    
    active = fields.Boolean(default=True)

    detail_id = fields.One2many(
    comodel_name='rindhiecounter.kategori', 
    inverse_name='stock_id', 
    string='Detail')

    @api.constrains('name')
    def _constrains_name(self):
        for rec in self:
            duplicate = self.env['rindhiecounter.handphone'].search([('name','=',rec.name)])
            if len(duplicate)>1:
                raise ValidationError("Merk Handphone %s Sudah Ada di Daftar!! %s" % (str(rec.name).upper(),str(len(duplicate))))
 
    @api.onchange('type')
    def _onchange_tipe(self):
        if self.type == 'android':
            return {
                'warning': {
                    'title' : 'Type Handphone',
                }
            }
        elif self.type == 'iphone':
            return {
                'warning': {
                    'title' : 'Type Handphone',
                }
            }

