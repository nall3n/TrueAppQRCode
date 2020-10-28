
function showMobileType() {

    if (/windows phone/i.test(navigator.userAgent)) {
        document.getElementById("status").innerHTML = "Windows phone";
    }

    else if (/android/i.test(navigator.userAgent)) {
        document.getElementById("status").innerHTML = "Android";
    }

    // iOS detection from: http://stackoverflow.com/a/9039885/177710
    else if (/iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream) {
        document.getElementById("status").innerHTML = "IPhone";
    }

    else {
        document.getElementById("status").innerHTML = "Datta";
    }

}

function redirect(){

    if (/windows phone/i.test(navigator.userAgent)) {
        document.getElementById("status").innerHTML = "Windows phone";
    }

    else if (/android/i.test(navigator.userAgent)) {
        document.getElementById("status").innerHTML = "Android";

        window.location = document.getElementById('android').innerHTML
    }

    // iOS detection from: http://stackoverflow.com/a/9039885/177710
    else if (/iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream) {
        document.getElementById("status").innerHTML = "iPhone";
        window.location = document.getElementById('iphone').innerHTML
    }

    else {
        document.getElementById("status").innerHTML = "Datta";
    }
}
