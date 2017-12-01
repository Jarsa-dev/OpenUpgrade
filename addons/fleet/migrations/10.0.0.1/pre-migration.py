# -*- coding: utf-8 -*-
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
    	env.cr, """
    	DELETE FROM res_groups WHERE category_id = (
    		SELECT id FROM ir_module_category WHERE name = 'Fleet')""")
