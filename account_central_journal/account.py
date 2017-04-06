# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 ISA s.r.l. (<http://www.isa.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import fields, models, api
from odoo.tools.translate import _
import decimal_precision as dp

class account_fiscalyear(models.Model):
    _inherit = "account.fiscalyear"
    _description = "Fiscal Year"

    date_last_print = fields.Date(string='Last printed date', readonly=True),
    progressive_page_number = fields.Integer(string='Progressive of the page', required=True, readonly=True),
    progressive_line_number = fields.Integer(string='Progressive line', required=True, readonly=True),
    progressive_credit = fields.Float(string='Progressive Credit', digits_compute=dp.get_precision('Account'), required=True, readonly=True),
    progressive_debit = fields.Float(string='Progressive Debit', digits_compute=dp.get_precision('Account'), required=True, readonly=True),
    
    _defaults = {
        'progressive_page_number': 0,
        'progressive_line_number': 0,
        'progressive_credit': lambda *a: float(),
        'progressive_debit': lambda *a: float(),
    }
