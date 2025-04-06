# Copyright 2025 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Fs Partner Multi Image",
    "summary": """
        Link images to partners""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "KMEE,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/storage",
    "depends": ["fs_base_multi_image", "base", "image_tag"],
    "data": [
        "security/fs_partner_image.xml",
        "views/fs_partner_image.xml",
        "views/res_partner.xml",
    ],
    "demo": [],
    "maintainers": ["mileo"],
    "development_status": "Alpha",
}
