odoo.define('dagoma_stock_barcode.LinesWidget', function (require) {

    "use strict";

    var LinesWidget = require('stock_barcode.LinesWidget');

    LinesWidget.include({
        events: _.extend(LinesWidget.prototype.events, {
            'click .o_barcode_scanner_inc_qty': '_onClickIncQty',
            'click .o_barcode_scanner_dec_qty': '_onClickDecQty'
        }),
        addProduct: function (lineDescription, model, doNotClearLineHighlight) {
            this._super.apply(this, arguments);
            var $line = this.$("[data-id='" + lineDescription.virtual_id + "']");
            $line.parents('.o_barcode_lines').toggleClass('o_js_has_highlight', true);
            $line.toggleClass('o_highlight', true);
            $line.toggleClass('o_highlight_green', false);
            $line.toggleClass('o_highlight_red', true);
        },
        incrementProduct: function(id_or_virtual_id, qty, model, doNotClearLineHighlight) {
            this._super(id_or_virtual_id, qty, model, true);

            var $line = this.$("[data-id='" + id_or_virtual_id + "']");

            var qtyDone = parseFloat($line.find('.qty-done').text());
            var todoQty = parseFloat($line.find('.qty-done ~ span:first').text().replace('/ ', ''));

            if (($line.data('highlight-warn') === 'highlight') || (!!todoQty && (qtyDone > todoQty))) {
                $line.parents('.o_barcode_lines').toggleClass('o_js_has_highlight', true);
                $line.toggleClass('o_highlight', true);
                $line.toggleClass('o_highlight_green', false);
                $line.toggleClass('o_highlight_red', true);
            }
        },
        _renderLines: function () {
            var result = this._super();

            var lines = this.getProductLines(this.page.lines);
            if (lines) {
                var $lines = this.$('.o_barcode_line');
                if (_.any($lines, function (el) {
                    return $(el).data('highlight-warn') === 'highlight';
                })) {
                    $lines.parents('.o_barcode_lines').toggleClass('o_js_has_highlight', true);
                }
            }

            return result;
        },
        _onClickIncQty: function (ev) {
            ev.preventDefault();

            var $target = $(ev.currentTarget);
            var $line = $target.parents('.o_barcode_line')

            var qty = parseFloat($line.data('step') || 1.0);

            this.incrementProduct($line.data('id'), qty, 'stock.picking');
        },
        _onClickDecQty: function (ev) {
            ev.preventDefault();

            var $target = $(ev.currentTarget);
            var $line = $target.parents('.o_barcode_line')

            var qty = parseFloat($line.data('step') || -1.0);
            var qtyDone = parseFloat($line.find('.qty-done').text());

            if (qtyDone + qty < 0.0) {
                return;
            }

            this.incrementProduct($line.data('id'), qty, 'stock.picking');
        }
    });

});
