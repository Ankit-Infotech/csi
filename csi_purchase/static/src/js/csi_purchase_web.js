odoo.define('csi_purchase.modify_delete_confrm_msg', function (require) {
"use strict";
var core = require('web.core');
var Dialog = require('web.Dialog');
var Model = require('web.DataModel');
var FormView = require('web.FormView');
var _t = core._t;
var QWeb = core.qweb;
var FieldOne2Many = core.form_widget_registry.get('one2many_list');
var Sidebar = require('web.Sidebar');
var data = require('web.data');
var List = core.view_registry.get('list');
var utils = require('web.utils');
var ListView = require('web.ListView');
var Class = core.Class;
var _t = core._t;
var _lt = core._lt;
var QWeb = core.qweb;
var list_widget_registry = core.list_widget_registry;

FormView.include({
    on_button_delete: function() {
    var self = this;
    var def = $.Deferred();
    var msg = 'Do you really want to delete this record?'
    this.has_been_loaded.done(function() {
        if (self.model == 'purchase.order')
        {
            msg = 'This will remove this PO from the system. Are you sure?'
        }
        if (self.datarecord.id && confirm(_t(msg))) {
            self.dataset.unlink([self.datarecord.id]).done(function() {
                if (self.dataset.size()) {
                    self.reload();
                    self.update_pager();
                } else {
                    self.do_action('history_back');
                }
                def.resolve();
            });
        } else {
            utils.async_when().done(function () {
                def.reject();
            });
        }
    });
    return def.promise();
    }
    })

ListView.include({
    do_delete: function (ids) {
    var self = this;
    var msg = 'Do you really want to remove these records?'
    var purchase = self.model
    if (purchase=='purchase.order')
    {
        msg = 'This will remove this PO from the system. Are you sure?'
    }

    if (!(ids.length && confirm(_t(msg)))) {
        return;
    }
    var self = this;

    return $.when(this.dataset.unlink(ids)).done(function () {
        _(ids).each(function (id) {
            self.records.remove(self.records.get(id));
        });
        // Hide the table if there is no more record in the dataset
        if (self.display_nocontent_helper()) {
            self.no_result();
        } else {
            if (self.records.length && self.current_min === 1) {
                // Reload the list view if we delete all the records of the first page
                self.reload();
            } else if (self.records.length && self.dataset.size() > 0) {
                // Load previous page if the current one is empty
                self.pager.previous();
            }
            // Reload the list view if we are not on the last page
            if (self.current_min + self._limit - 1 < self.dataset.size()) {
                self.reload();
            }
        }
        self.update_pager(self.dataset);
        self.compute_aggregates();
    });
},
})

})