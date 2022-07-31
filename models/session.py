# -*- coding: utf-8 -*-

# from dataclasses import field
from datetime import timedelta
from xml.dom import ValidationErr
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ghoziacademy(models.Model):
    _name = 'ghozi_academy.session'
    _description = 'Session of Course Ghozi Academy'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')
    start_date = fields.Date(string='Start Date', default= fields.Date.today)
    duration = fields.Float(string='Duration')
    number_of_seats = fields.Float(string='Number of Seats')
    user_id = fields.Many2one(string='Instructor', comodel_name='res.users', domain="['|',('is_instructor','=', True),('teacher_category_id', '!=', False)]")
    attendee_ids = fields.Many2many(comodel_name='res.users', string='Attendees')
    attendees_count = fields.Integer(string='Jumlah Peserta', store=True, compute='_get_attendees_count')
    course_id = fields.Many2one(string='Course', comodel_name='ghozi_academy.course')
    taken_seats = fields.Float(sting="Taken seats", compute='_compute_taken_seats')
    color = fields.Integer()

    # rec.taken_seats = 100.0 * len(rec.attendee_ids)/rec.number_of_seats

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    @api.depends('attendee_ids','number_of_seats')
    def _compute_taken_seats(self):
        for rec in self:
            if rec.number_of_seats < 1 or len(rec.attendee_ids) < 1:
                rec.taken_seats = 0.0
            else:
                rec.taken_seats = 100.0 * len(rec.attendee_ids)/rec.number_of_seats
    
    @api.depends('number_of_seats', 'attendee_ids')
    def _cek_data_valid(self):
        if self.number_of_seats < 0 :
            return {
                    'warning':
                        {
                        'title': "Invalid Values",
                        'messages': "Negative Number of Seats",
                        }
            }
        if self.number_of_seats < len(self.attendee_ids):
            return {
                    'warning':
                        {
                        'title': "Something Bad",
                        'message': "Attendees Overload",
                        }
            }            
    
    @api.constrains('user_id','attendee_ids')
    def validasi_user_attendee(self):
        for r in self:
            if r.user_id and r.user_id in r.attendee_ids:
                raise ValidationError('Mohon maaf instruktur tidak dapat mendaftar sebagai peserta')
    
    
    @api.depends('attendee', 'duration')
    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue
            r.duration =(r.end_date - r.start_date).days + 1
    
    @api.depends('start_date','duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            duration = timedelta(days=r.duration, seconds= -1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue
            r.duration=(r.end_date - r.start_date).days + 1