odoo.define('csi_account.csi_account_web', function (require) {
"use strict";
var ActionManager = require('account.reconciliation');
var core = require('web.core');
var QWeb = core.qweb;
var _t = core._t;
var FieldMany2One = core.form_widget_registry.get('many2one');
console.log('gggggg',ActionManager)
   ActionManager.bankStatementReconciliationLine = ActionManager.bankStatementReconciliationLine.include({
   createFormWidgets: function() {
        var self = this;
        this._super();
        self.change_partner_field.destroy();
        // generate the change partner "form"
        var change_partner_field = {
            relation: "res.partner",
            string: _t("Partner"),
            type: "many2one",
            domain: [['parent_id','=',false], '|', ['customer','=',true], ['supplier','=',true]],
            help: "",
            readonly: false,
            required: true,
            selectable: true,
            states: {},
            views: {},
            context: {},
        };
        var change_partner_node = {
            tag: "field",
            children: [],
            required: true,
            attrs: {
                invisible: "False",
                modifiers: '',
                name: "change_partner",
                nolabel: "True",
            }
        };
        self.field_manager.fields_view.fields["change_partner"] = change_partner_field;
        self.change_partner_field = new FieldMany2One(self.field_manager, change_partner_node);
        self.change_partner_field.options['no_create_edit','no_create'] = 'True'

        self.change_partner_field.appendTo(self.$(".change_partner_container"));
        self.change_partner_field.on("change:value", self.change_partner_field, function() {
            self.changePartner(this.get_value());
        });
        self.change_partner_field.$el.find("input").attr("placeholder", self.st_line.communication_partner_name || _t("Select Partner"));
    },

});

});