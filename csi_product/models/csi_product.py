# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = "product.template"

    """ Create Reorder rule when product create """
    @api.model
    def create(self,vals):
        res = super(ProductTemplate, self).create(vals)
        warehouse_rec = self.env['stock.warehouse'].search([])
        product_id = self.env['product.product'].search([('product_tmpl_id','=',res.id)])
        if not self.env.context.get('create_product_product'):
            if vals.get('name'):
                reorder_obj = self.env['stock.warehouse.orderpoint']
                for warehouse in warehouse_rec:
                    reorder_vals = {
                                    'product_id':product_id.id,
                                    'product_min_qty':0.0,
                                    'product_max_qty':0.0,
                                    'warehouse_id':warehouse.id,
                                    'location_id':warehouse.lot_stock_id.id
                    }
                    reorder_obj.create(reorder_vals)
        return res
    """ End of code """

    """ Set value of invoice policy based on product type """
    @api.onchange('type')
    def _onchange_type(self):
        if self.type and self.type == 'service':
            self.invoice_policy = 'order'
        if self.type and self.type == 'product':
            self.invoice_policy = 'delivery'
    """ End of code """

class ProductProduct(models.Model):
    _inherit = 'product.product'

    """ Create Reorder rule when product create """
    @api.model
    def create(self,vals):
        res = super(ProductProduct, self).create(vals)
        wo_id = self.env['stock.warehouse'].search([])
        if vals.get('name'):
            reorder_obj = self.env['stock.warehouse.orderpoint']
            for warehouse in wo_id:
                reorder_vals = {
                                'product_id':res.id,
                                'product_min_qty':0.0,
                                'product_max_qty':0.0,
                                'warehouse_id':warehouse.id,
                                'location_id':warehouse.lot_stock_id.id
                }
                reorder_obj.create(reorder_vals)
        return res
    """ End of code """

    """ set value of invoice policy based on product type """
    @api.onchange('type')
    def _onchange_type(self):
        if self.type and self.type == 'service':
            self.invoice_policy = 'order'
        if self.type and self.type == 'product':
            self.invoice_policy = 'delivery'
    """ End of code """