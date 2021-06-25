from odoo import api, fields, models
import time

class Course(models.Model):
    _name = "academic.course"

    name = fields.Char("Name", required=True, size=100)
    description = fields.Text("Description")
    responsible_id = fields.Many2one(
        comodel_name="res.partner",
        string="Responsible",
        required=True)
    session_ids = fields.One2many(
        comodel_name="academic.session",
        string="sessions",
        inverse_name="course_id")

_sql_constraints = [
        ('sql_cek_name', 'UNIQUE(name)', 'Nama kursus tidak boleh duplikat!'),
        ('sql_cek_desc', 'CHECK(name <> description)', 'Nama tidak boleh sama dengan deskripsi!')
]
