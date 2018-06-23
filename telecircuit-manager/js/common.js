$(function () {
    $('.header-menu').slicknav({
        label: 'TELECIRCUIT',
    });
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('#scroll-to-top').fadeIn();
        } else {
            $('#scroll-to-top').fadeOut();
        }
    });

    //Click event to scroll to top
    $('#scroll-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 800);
        return false;
    });
    $('.model-components-list-header a').each(function () {
        var location = window.location.href;
        var link = this.href;
        if (location == link) {
            $(this).css({
                'background': '#41508C',
                'color': '#fff'
            });
        }
    });

});
