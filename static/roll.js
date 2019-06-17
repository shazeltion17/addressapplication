function Rollme() {

    const template = Handlebars.compile("<li>You Rolled a <img src=\"/static/img/{{value}}.PNG\"></li>");
    const roll = Math.floor((Math.random()*6) + 1)
    const content = template({'value' : roll});
    document.querySelector('#rolls').innerHTML += content

}

