/* Toggle Form functionality. Wraps a form inside a popover. Used for advanced search. */

(function($) {
    $('.arctic_toggle_form_button').each(function(){
        var selector = $(this).data('popover_content_container');
        var form = $(selector).contents();

        $(this).data('form', form);
    }).popover({
        content: function () {
            return $(this).data('form');
        },
        html: true
    });


    var dismissOnClick = function () {
        $('body').on('click.popover', function(e) {
            var target = e.target;
            if (!$(target).is('.popover') &&
                !$(target).parents().is('.popover') &&
                !$(target).is('.arctic_toggle_form_button') &&
                !$(target).parents().is('.arctic_toggle_form_button')
                ) {
                $('body').off('click.popover');
                $('.arctic_toggle_form_button').popover('hide');
            }
        });
    }
    $('.arctic_toggle_form_button').on('show.bs.popover', dismissOnClick);
})(jQuery);
