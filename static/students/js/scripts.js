$(document).ready(function() {
    // Highlight the active page on navbar
    let currentUrl = window.location.href;
    $('.navbar-nav .nav-item a').each(function() {
        if (this.href === currentUrl) {
            $(this).closest('.nav-item').addClass('active');
        }
    });
    $('#registrationForm').on('keyup', '#id_password, #id_password_confirm', function() {
        const password = $('#id_password').val();
        const passwordConfirm = $('#id_password_confirm').val();
        if (password && passwordConfirm && password !== passwordConfirm) {
            $('#id_password_confirm')[0].setCustomValidity('Passwords do not match!');
        } else {
            $('#id_password_confirm')[0].setCustomValidity('');
        }
    });
});
