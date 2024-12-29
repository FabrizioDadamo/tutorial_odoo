from odoo import models, fields

class ProgressModel(models.Model):
    _name = 'progress.model'
    _description = 'Progresso Utente'

    user_id = fields.Many2one('res.users', string="Utente", required=True)
    tutorial_id = fields.Many2one('tutorial.model', string="Tutorial", required=True)
    is_completed = fields.Boolean(string="Completato", default=False)
