# Copyright 2025 KMEE
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import api, fields, models


class ImageTag(models.Model):
    _inherit = "image.tag"

    @api.model
    def _get_default_apply_on(self):
        active_model = self.env.context.get("active_model")
        if active_model == "res.partner.image.relation":
            return "partner"
        else:
            return super()._get_default_apply_on()

    apply_on = fields.Selection(
        selection_add=[("partner", "Partner")],
        ondelete={"partner": "cascade"},
    )
