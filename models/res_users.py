# -*- coding: utf-8 -*-

import string
from typing_extensions import Required
from odoo import models, fields, api

class TeacherCategory(models.Model):
    _name='ghozi_academy.teacher_category'

    name = fields.Char(string="name")

class UserInherit(models.Model):
    _inherit = 'res.users'

    is_instructor = fields.Boolean(string="Instructor?")
    session_ids = fields.One2many(string='Sessions', comodel_name='ghozi_academy.session', inverse_name='user_id')
    teacher_category_id = fields.Many2one(string="Teacher Category", comodel_name='ghozi_academy.teacher_category')