(function () {
  var navToggle = document.getElementById('navToggle');
  var siteNav = document.getElementById('siteNav');

  if (navToggle && siteNav) {
    navToggle.addEventListener('click', function () {
      var isOpen = siteNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    siteNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        siteNav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  var countdownEl = document.getElementById('countdown');
  if (countdownEl) {
    var workshopStart = new Date('2026-11-02T00:00:00-05:00');

    function updateCountdown() {
      var now = new Date();
      var diffMs = workshopStart - now;

      if (diffMs <= 0) {
        countdownEl.textContent = '';
        return;
      }

      var days = Math.ceil(diffMs / (1000 * 60 * 60 * 24));
      countdownEl.textContent = days + (days === 1 ? ' day' : ' days') + ' until the workshop';
    }

    updateCountdown();
  }
})();
