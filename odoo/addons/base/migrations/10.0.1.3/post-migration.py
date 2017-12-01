# coding: utf-8
# © 2017 Opener BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    openupgrade.load_data(
        env.cr, 'base', 'migrations/10.0.1.3/noupdate_changes.xml'
    )
    modules = env['ir.module.module'].search([('state', '=', 'uninstalled')])
    modules.unlink()
    env.cr.execute("DELETE FROM ir_model_data WHERE name='module_web' AND module='base'")
    env['ir.module.module'].update_list()
    env.cr.commit()
