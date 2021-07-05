from odoo import fields, models, api

class PinjamDetil(models.Model):
    _name = 'perpus.pinjamdetil'
            
    pinjam_id = fields.Many2one(
        comodel_name="perpus.pinjam",
        string="Pinjaman")
    buku_id = fields.Many2one(
        comodel_name="perpus.buku",
        string="Judul Buku")
    jumlah = fields.Integer("Jumlah")
