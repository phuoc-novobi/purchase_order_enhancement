odoo.define('purchase.phone.us.widget', function (require) {
    'use strict';

    var FieldChar = require('web.basic_fields').FieldChar;
    var field_registry = require('web.field_registry');

    function normalize(phone) {
        phone = phone.replace(/[^\d]/g, "");
        if (phone.length == 10) {
            return phone.replace(/(\d{3})(\d{3})(\d{4})/, "($1) $2-$3");
        }
        return phone;
    }

    var USPhoneNumber = FieldChar.extend({
        events: _.extend({}, FieldChar.prototype.events, {
            'keyup': '_onKeyup',
        }),
        _onKeyup: function (e) {
            e.target.value = normalize(e.target.value)
            console.log('event happen!')
        }
    });

    field_registry.add("us_phone_number_wget", USPhoneNumber);
    return USPhoneNumber;
})
