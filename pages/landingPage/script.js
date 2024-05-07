console.log("script loaded")

var topbar = document.getElementById("topbar");
var prevScrollpos = window.pageYOffset;

window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        topbar.style.top = "0";
    } else {
        topbar.style.top = "-200px";
    }
    prevScrollpos = currentScrollPos;
}

var mouseNearTopbar = false;

topbar.addEventListener("mouseenter", function() {
    mouseNearTopbar = true;
    topbar.style.top = "0";
});

topbar.addEventListener("mouseleave", function() {
    mouseNearTopbar = false;
    if (prevScrollpos <= 0) {
        topbar.style.top = "0";
    } else {
        topbar.style.top = "-200px";
    }
});

window.addEventListener("mousemove", function(event) {
    var y = event.clientY;
    if (!mouseNearTopbar && y < 170) { // Adjustee comme besois pour la sensi de la bar
        topbar.style.top = "0";
    } else if (!mouseNearTopbar && prevScrollpos > 0) {
        topbar.style.top = "-200px";
    }
});
