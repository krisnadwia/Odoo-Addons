from odoo import fields, models, api
import time

class Pinjam(models.Model):
    _name ='perpus.pinjam'
    _order = 'tgl_pinjam desc'

    tgl_pinjam = fields.Date("Tanggal Pinjam", default=lambda self: time.strftime("%Y-%m-%d"))   
    pinjamdetil_ids = fields.One2many(
        comodel_name="perpus.pinjamdetil",
        string="Buku Yang Dipinjam",
        inverse_name="pinjam_id")
