from odoo import api, fields, models

class Attendee(models.Model):
    _name = "academic.attendee"

    session_id = fields.Many2one(comodel_name="academic.session",
        string="Pertemuan")

    partner_id = fields.Many2one(comodel_name="res.partner",
        string="Mahasiswa")

    # constraint = batasan
    # sql_constraint diatur dalam database Postgre
    _sql_constraints = [
        ('sql_cek_attendee', 'UNIQUE(session_id, partner_id)', 'Peserta dalam suatu sesi tidak boleh double!')
    ]
