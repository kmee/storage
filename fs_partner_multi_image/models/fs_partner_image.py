# Copyright 2025 KMEE
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FsProductBrandImage(models.Model):
    _name = "fs.res.partner.image"
    _inherit = "fs.image.relation.mixin"
    _description = "Partner Image"

    partner_id = fields.Many2one(
        "res.partner",
        required=True,
        ondelete="cascade",
    )
    tag_id = fields.Many2one(
        "image.tag",
        string="tag",
        domain=[("apply_on", "=", "partner")],
    )
