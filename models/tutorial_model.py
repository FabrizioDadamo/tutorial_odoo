from odoo import models, fields, api

class TutorialModel(models.Model):
    _name = 'tutorial.model'
    _description = 'Gestione dei Tutorial'
    _order = 'sequence'

    name = fields.Char(string="Titolo", required=True)
    content = fields.Html(string="Contenuto", required=True)
    description = fields.Text(string="Descrizione")
    is_completed = fields.Boolean(string="Completato", default=False)
    sequence = fields.Integer("Sequenza", default=10)
    created_date = fields.Datetime(string="Creato il", default=fields.Datetime.now, readonly=True)
    updated_date = fields.Datetime(string="Ultima Modifica", readonly=True)

    @api.onchange('content')
    def _update_date(self):
        """Aggiorna la data di modifica ogni volta che il contenuto cambia."""
        self.updated_date = fields.Datetime.now()
