$(document).ready(function(){

  $('.post-wrapper').slick({

    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 2000,
    nextArrow: $('.next'),
    prevArrow: $('.prev'),
  });
});

$(document).ready(function(){

  $('.post-wrapper-action').slick({

    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 2000,
    nextArrow: $('.next-action'),
    prevArrow: $('.prev-action'),
  });
});


$(document).ready(function(){

  $('.post-wrapper-horror').slick({

    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 2000,
    nextArrow: $('.next-horror'),
    prevArrow: $('.prev-horror'),
  });
});
$(document).ready(function(){

  $('.post-wrapper-fantasy').slick({

    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 2000,
    nextArrow: $('.next-fantasy'),
    prevArrow: $('.prev-fantasy'),
  });
});
// navbar
document.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");
  const navbarHeight = 100;

  const distanceFromTop = Math.abs(
    document.body.getBoundingClientRect().top
  );

  if (distanceFromTop >= navbarHeight) navbar.classList.add("fixed-top");
  else navbar.classList.remove("fixed-top");
});