/*
* Greedy Navigation
*
* http://codepen.io/lukejacksonn/pen/PwmwWV
*
*/

var $nav = $('#site-nav');
var $btn = $('#site-nav button');
var $vlinks = $('#site-nav .visible-links');
var $hlinks = $('#site-nav .hidden-links');

function updateNav() {
  // Start from the full list so one resize can restore every item that fits.
  $vlinks.append($hlinks.children());
  $btn.addClass('hidden');

  if ($vlinks.outerWidth() > $nav.width()) {
    $btn.removeClass('hidden');
    var gap = parseFloat($nav.css('font-size')) || 16;
    var availableSpace = $nav.width() - $btn.outerWidth() - gap;

    while ($vlinks.children().length > 1 && $vlinks.outerWidth() > availableSpace) {
      $vlinks.children().last().prependTo($hlinks);
    }
  }

  var hiddenCount = $hlinks.children().length;
  $btn.attr('count', hiddenCount);
  if (!hiddenCount) {
    $btn.addClass('hidden').removeClass('close');
    $hlinks.addClass('hidden');
  }
  $btn.attr('aria-expanded', !$hlinks.hasClass('hidden'));
}

// Window listeners

$(window).resize(function() {
  updateNav();
});

$btn.on('click', function() {
  $hlinks.toggleClass('hidden');
  $(this).toggleClass('close').attr('aria-expanded', !$hlinks.hasClass('hidden'));
});

updateNav();