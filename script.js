document.addEventListener('DOMContentLoaded', function() {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const menu = document.querySelector('.header .row');
    const header = document.getElementById('home');
    const body = document.querySelector('body');

    function toggleMenu(event) {
        event.stopPropagation();
        menu.classList.toggle('show');
        header.classList.toggle('responsive-header');
    }

    // Toggle menu on hamburger icon click
    hamburgerMenu.addEventListener('click', toggleMenu);

    // Close menu on outside click
    menu.addEventListener('click', toggleMenu);
});
