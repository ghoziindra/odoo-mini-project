
from odoo import models, fields, api

class WizardAttendees(models.TransientModel):
    _name = 'ghozi_academy.wizard_attendees'
    _description = 'ghozi_academy.wizard_attendees'

    session_id = fields.Many2one(comodel_name='ghozi_academy.session', string="Session")
    attendee_ids = fields.Many2many(comodel_name='res.user', string="Attendees")

    def subscribe(self):
        self.session_id.attende_ids |= self.attendee_ids
        return{}


# 'Wizard: Quick Registration of Attendees to Session'