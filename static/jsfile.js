function displayError() {

        var x = document.getElementById("errortext");
        var address_text = document.getElementById("input1").value;
        const request = new XMLHttpRequest();
        const data = new FormData();
        data.append('address', address_text)

        if (address_text === "") {
            x.style.display = "block";
        } else {
            x.style.display = "block";
            request.open('POST', '/address')
            request.send(data)
            request.onload = () => {
                const data = JSON.parse(request.responseText)
                console.log(data)
                if (data == 'There is no addresses present') {
                    x.innerHTML = data
                } else  {
                    x.innerHTML = "This has been updated in the database"
                }
            }
        }
    }