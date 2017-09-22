# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenUpgrade module for Odoo
#    @copyright 2014-Today: Odoo Community Association
#    @author: Sylvain LE GAL <https://twitter.com/legalsylvain>
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

from openerp.openupgrade import openupgrade
from openerp.addons.openupgrade_records.lib import apriori

xml_ids = [
    ('portal.group_anonymous', 'base.group_public'),
    ('portal.group_portal', 'base.group_portal'),
    ('l10n_gt.GTQ', 'base.GTQ'),
    ('l10n_gt.rateGTQ', 'base.rateGTQ'),
]


def cleanup_modules(cr):
    """Don't report as missing these modules, as they are integrated in
    other modules."""

    openupgrade.update_module_names(
        cr, [
            # from OCA/product-attribute
            ('product_customer_code', 'product_supplierinfo_for_customer'),
            # from OCA/sale-workflow - included in core
            ('sale_multi_picking', 'sale_sourced_by_line'),
            # from OCA/stock-logistics-workflow
            ('stock_cancel', 'stock_picking_back2draft'),
        ], merge_modules=True,
    )


@openupgrade.migrate()
def migrate(cr, version):
    # Drop view that inhibits changing field types. It will be recreated BTW

    # PIEZA, PIEZA & P to Unit(s) product_template
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uom_id = 1
        WHERE uom_id in (16, 41, 42);
        """)
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uos_id = 1
        WHERE uos_id in (16, 41, 42);
        """)
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uom_po_id = 1
        WHERE uom_po_id in (16, 41, 42);
        """)
     # PIEZA, PIEZA & P to Unit(s) procurement_order
    openupgrade.logged_query(
        cr, """
        UPDATE procurement_order
        SET product_uom = 1
        WHERE product_uom in (16, 41, 42);
        """)
    # PIEZA, PIEZA & P to Unit(s) purchase order line
    openupgrade.logged_query(
        cr, """
        UPDATE purchase_order_line
        SET product_uom = 1
        WHERE product_uom in (16, 41, 42);
        """)
    # PIEZA, PIEZA & P to Unit(s) sale order line
    openupgrade.logged_query(
        cr, """
        UPDATE sale_order_line
        SET product_uom = 1
        WHERE product_uom in (16, 41, 42);
        """)
    # PIEZA, PIEZA & P to Unit(s) stock inventory line
    openupgrade.logged_query(
        cr, """
        UPDATE stock_inventory_line
        SET product_uom = 1
        WHERE product_uom in (16, 41, 42);
        """)
    # PIEZA, PIEZA & P to Unit(s) stock move
    openupgrade.logged_query(
        cr, """
        UPDATE stock_move
        SET product_uom = 1
        WHERE product_uom in (16, 41, 42);
        """)
    # SERVICIO, SERVICIO to Servicio product_template
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uom_id = 19
        WHERE uom_id in (15, 40);
        """)
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uos_id = 19
        WHERE uos_id in (15, 40);
        """)
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uom_po_id = 19
        WHERE uom_po_id in (15, 40);
        """)
     # SERVICIO, SERVICIO & Servicio to Unit(s) procurement_order
    openupgrade.logged_query(
        cr, """
        UPDATE procurement_order
        SET product_uom = 19
        WHERE product_uom in (15, 40);
        """)
    # SERVICIO, SERVICIO & Servicio to Unit(s) purchase order line
    openupgrade.logged_query(
        cr, """
        UPDATE purchase_order_line
        SET product_uom = 19
        WHERE product_uom in (15, 40);
        """)
    # SERVICIO, SERVICIO & Servicio to Unit(s) sale order line
    openupgrade.logged_query(
        cr, """
        UPDATE sale_order_line
        SET product_uom = 19
        WHERE product_uom in (15, 40);
        """)
    # SERVICIO, SERVICIO & Servicio to Unit(s) stock inventory line
    openupgrade.logged_query(
        cr, """
        UPDATE stock_inventory_line
        SET product_uom = 19
        WHERE product_uom in (15, 40);
        """)
    # SERVICIO, SERVICIO & Servicio to Unit(s) stock move
    openupgrade.logged_query(
        cr, """
        UPDATE stock_move
        SET product_uom = 19
        WHERE product_uom in (15, 40);
        """)
    # Juegos to Juego product_template
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uom_id = 30
        WHERE uom_id in (14, 20);
        """)
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uos_id = 30
        WHERE uos_id in (14, 20);
        """)
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uom_po_id = 30
        WHERE uom_po_id in (14, 20);
        """)
     # Juegos to Juego procurement_order
    openupgrade.logged_query(
        cr, """
        UPDATE procurement_order
        SET product_uom = 30
        WHERE product_uom in (14, 20);
        """)
    # Juegos to juego purchase order line
    openupgrade.logged_query(
        cr, """
        UPDATE purchase_order_line
        SET product_uom = 30
        WHERE product_uom in (14, 20);
        """)
    # Juegos to juego sale order line
    openupgrade.logged_query(
        cr, """
        UPDATE sale_order_line
        SET product_uom = 30
        WHERE product_uom in (14, 20);
        """)
    # Juegos to juego stock inventory line
    openupgrade.logged_query(
        cr, """
        UPDATE stock_inventory_line
        SET product_uom = 30
        WHERE product_uom in (14, 20);
        """)
    # Juegos to juego stock move
    openupgrade.logged_query(
        cr, """
        UPDATE stock_move
        SET product_uom = 30
        WHERE product_uom in (14, 20);
        """)
    # Herramienta   product_template
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uom_id = 44
        WHERE uom_id = 43;
        """)
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uos_id = 44
        WHERE uos_id = 43;
        """)
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uom_po_id = 44
        WHERE uom_po_id = 43;
        """)
     # Herramienta  procurement_order
    openupgrade.logged_query(
        cr, """
        UPDATE procurement_order
        SET product_uom = 44
        WHERE product_uom = 43;
        """)
    # Herramienta   purchase order line
    openupgrade.logged_query(
        cr, """
        UPDATE purchase_order_line
        SET product_uom = 44
        WHERE product_uom = 43;
        """)
    # Herramienta   sale order line
    openupgrade.logged_query(
        cr, """
        UPDATE sale_order_line
        SET product_uom = 44
        WHERE product_uom = 43;
        """)
    # Herramienta   stock inventory line
    openupgrade.logged_query(
        cr, """
        UPDATE stock_inventory_line
        SET product_uom = 44
        WHERE product_uom = 43;
        """)
    # Herramienta   stock move
    openupgrade.logged_query(
        cr, """
        UPDATE stock_move
        SET product_uom = 44
        WHERE product_uom = 43;
        """)
    # Litros product_template
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uom_id = 11
        WHERE uom_id = 33;
        """)
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uos_id = 11
        WHERE uos_id = 33;
        """)
    openupgrade.logged_query(
        cr, """
        UPDATE product_template
        SET uom_po_id = 11
        WHERE uom_po_id = 33;
        """)
     # Litrosprocurement_order
    openupgrade.logged_query(
        cr, """
        UPDATE procurement_order
        SET product_uom = 11
        WHERE product_uom = 33;
        """)
    # Litros purchase order line
    openupgrade.logged_query(
        cr, """
        UPDATE purchase_order_line
        SET product_uom = 11
        WHERE product_uom = 33;
        """)
    # Litros sale order line
    openupgrade.logged_query(
        cr, """
        UPDATE sale_order_line
        SET product_uom = 11
        WHERE product_uom = 33;
        """)
    # Litros stock inventory line
    openupgrade.logged_query(
        cr, """
        UPDATE stock_inventory_line
        SET product_uom = 11
        WHERE product_uom = 33;
        """)
    # Litros stock move
    openupgrade.logged_query(
        cr, """
        UPDATE stock_move
        SET product_uom = 11
        WHERE product_uom = 33;
        """)
    # Delete Unused Uoms 
    openupgrade.logged_query(
        cr, """
        DELETE FROM product_uom
        WHERE id in (16, 41, 42, 15, 40, 14, 20, 43, 33);
        """)
    cr.execute(
    str("""SELECT sil.id, sil.product_id, pc.id category_id FROM stock_inventory_line sil
        JOIN product_uom pu ON pu.id = sil.product_uom
        JOIN product_uom_categ pc ON pc.id = pu.category_id"""))
    data = cr.fetchall()
    for rec in data:
        cr.execute(str(
            """SELECT pc.id category_id, pt.uom_id FROM stock_inventory_line sil
            JOIN product_product pp ON pp.id = sil.product_id
            JOIN product_template pt ON pt.id = pp.product_tmpl_id
            JOIN product_uom pu ON pu.id = pt.uom_id
            JOIN product_uom_categ pc ON pc.id = pu.category_id
            WHERE sil.id = %s""") % (rec[0]))
        line = cr.fetchall()
        if line[0][0] != rec[2]:
            cr.execute(str("""
                UPDATE stock_inventory_line
                SET product_uom = %s
                WHERE id = %s""") % (line[0][1], rec[0]))
    cr.execute(
    str("""SELECT sm.id, sm.product_id, pc.id category_id FROM stock_move sm
        JOIN product_uom pu ON pu.id = sm.product_uom
        JOIN product_uom_categ pc ON pc.id = pu.category_id"""))
    data2 = cr.fetchall()
    for rec in data2:
        cr.execute(str(
            """SELECT pc.id category_id, pt.uom_id FROM stock_move sm
            JOIN product_product pp ON pp.id = sm.product_id
            JOIN product_template pt ON pt.id = pp.product_tmpl_id
            JOIN product_uom pu ON pu.id = pt.uom_id
            JOIN product_uom_categ pc ON pc.id = pu.category_id
            WHERE sm.id = %s""") % (rec[0]))
        line = cr.fetchall()
        if line[0][0] != rec[2]:
            cr.execute(str("""
                UPDATE stock_move
                SET product_uom = %s
                WHERE id = %s""") % (line[0][1], rec[0]))
    cr.execute('drop view if exists report_document_user cascade')

    openupgrade.update_module_names(
        cr, apriori.renamed_modules.iteritems()
    )
    openupgrade.rename_xmlids(cr, xml_ids)
    openupgrade.check_values_selection_field(
        cr, 'ir_act_report_xml', 'report_type',
        ['controller', 'pdf', 'qweb-html', 'qweb-pdf', 'sxw', 'webkit'])
    openupgrade.check_values_selection_field(
        cr, 'ir_ui_view', 'type', [
            'calendar', 'diagram', 'form', 'gantt', 'graph', 'kanban',
            'qweb', 'search', 'tree'])
    
    # The tables stock.picking.in and stock.picking.out are merged into 
    # stock.picking
    openupgrade.logged_query(
        cr, """
        UPDATE ir_attachment
        SET res_model = 'stock.picking'
        WHERE res_model in ('stock.picking.in', 'stock.picking.out');
        """)
    
    # Product.template is used for non variant product in v7 this was
    # product.product
    openupgrade.logged_query(
        cr, """
        UPDATE ir_attachment
        SET res_model = 'product.template'
        WHERE res_model = 'product.product';
        """)

    cleanup_modules(cr)
