# Copyright 2025 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.fs_image.fields import FSImage


class ResPartner(models.Model):
    _inherit = "res.partner"

    image_ids = fields.One2many(
        string="Images",
        comodel_name="fs.res.partner.image",
        inverse_name="partner_id",
    )
    image = FSImage(related="image_ids.image", readonly=True, store=False)
    image_medium = FSImage(related="image_ids.image_medium", readonly=True, store=False)
