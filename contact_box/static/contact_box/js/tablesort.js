$( document ).ready(function() {

    let orderManager = $('#order-manager');
    let orderby = orderManager.data('orderby');
    let order = orderManager.data('order');
    let search = orderManager.data('search');

    if ((orderby !== undefined) && (order !== undefined)) {
        let sortElements = $('.order');
        sortElements.each(function() {
            let sortElementOrderBy = $(this).data('orderby');
            let sortElementOrder = $(this).data('order');
            let href = $(this).attr('href');
            let newHref = href + '&orderby=' + sortElementOrderBy + '&order=' + sortElementOrder;
            if (search != "None") newHref += '&search=' + search;
            $(this).attr('href', newHref);
            if ((sortElementOrderBy == orderby) && (sortElementOrder == order)) {
                $(this).addClass('order-active')
            }
        })
    }

});