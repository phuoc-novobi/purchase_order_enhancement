odoo.define('purchase_order_enhancement.phone_us_widget', function (require) {
    'use strict';

    var FieldChar = require('web.basic_fields').FieldChar;
    var field_registry = require('web.field_registry');

    var USPhoneNumber = FieldChar.extend({
        events: _.extend({}, FieldChar.prototype.events, {
            'keyup': '_onKeyup',
        }),
        _onKeyup: function (e) {
            let phone = e.target.value;
            // A normalize phone number function found on https://stackoverflow.com
            phone = phone.replace(/[^\d]/g, "");
            if (phone.length === 10)
                phone = phone.replace(/(\d{3})(\d{3})(\d{4})/, "($1) $2-$3");
            e.target.value = phone;
        }
    });

    field_registry.add("us_phone_number_wget", USPhoneNumber);
    return USPhoneNumber;
})
