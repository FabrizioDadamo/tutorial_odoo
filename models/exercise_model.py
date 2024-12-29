from odoo import models, fields

class ExerciseModel(models.Model):
    _name = 'exercise.model'
    _description = 'Esercizi per Tutorial'

    name = fields.Char(string="Domanda", required=True)
    tutorial_id = fields.Many2one('tutorial.model', string="Tutorial", required=True)
    hint = fields.Text(string="Suggerimento")
    answer = fields.Text(string="Risposta")
