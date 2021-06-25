from odoo import api, fields, models
import time

class Session(models.Model):
    _name = "academic.session"

    name = fields.Char("Name", required=True, size=100)
    course_id = fields.Many2one(
        comodel_name="academic.course",
        string="Course")
    start_date = fields.Date("Start Date", 
        default=lambda self: time.strftime("%Y-%m-%d"))    
    duration = fields.Integer("Duration")
    seats = fields.Integer("Seats")
    active = fields.Boolean("Is Active", default=True)
    attendee_ids = fields.One2many(
        comodel_name="academic.attendee",
        string="Daftar Hadir",
        inverse_name="session_id")
    taken_seats = fields.Float(name="Taken Seat", 
        compute="_hitung_prosentase_kehadiran")
    state = fields.Selection(
        String="State",
        selection=[
            ('df','Draft'),
            ('cf','Confirmed'),
            ('dn','Done')
        ],
        readonly=True,
        required=True,
        default='df'
    )

    @api.multi
    def action_confirm(self):
        self.state = 'cf'
    
    @api.multi
    def action_approve(self):
        self.state = 'dn'

    @api.multi
    def action_reject(self):
        self.state = 'df'

    def _hitung_prosentase_kehadiran(self):
        for x in self:
            if x.seats > 0:
                x.taken_seats = 100.00 * len(x.attendee_ids) / x.seats
            else:
                x.taken_seats = 0

    def _cek_instruktur(self):
        for session in self:
            # 1. Menampung semua ID Mahasiswa yg terdaftar di session tsb    
            x = []
            for mhs in session.attendee_ids:
                x.append(mhs.partner_id.id)
        # 2. Cek, apakah ID Instruktur ada di daftar ID Mahasiswa?
        if session.course_id.responsible_id.id in x:
            return False
        return True 

    # format=(nama_fungsi, pesan jika Error/False, field-field yg dicek)
    _constraints = [
        (
            _cek_instruktur, 
            'instruktur tidak boleh menjadi peserta', 
            ['course_id','attendee_ids']
        )
    ]
