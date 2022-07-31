# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import models, fields, api


class ghoziacademy(models.Model):
    _name = 'ghozi_academy.course'
    _description = 'Course of Ghozi Academy'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    user_id = fields.Many2one(string='Responsible User', comodel_name='res.users')
    session_ids = fields.One2many(string='Session', comodel_name='ghozi_academy.session', inverse_name='course_id')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
