var submitButton = document.getElementById("submitButton")
submitButton.addEventListener("click", submit_request);

function update_pgbar(perc){
    var pgbar = document.querySelector('#progress-bar');
    pgbar.style.width = "25%"
}

function submit_request() {
    console.log("work");
    var pgbar = document.querySelector('#progress')

    pgbar.classList.toggle('d-none')

    setTimeout(update_pgbar,20000)

    event.preventDefault()
    const userInput = document.getElementById("message").value;

    // console.log(eventname,instname,startdate,enddate,prize,level,cashprize)

    var formdata = new FormData();
    formdata.append("userInput", userInput);

    var requestOptions = {
        method: "POST",
        body: formdata,
        redirect: "follow"
    };

    fetch("/submit/", requestOptions)
        .then((response) => response.text())
        .then((result) => {
            console.log(result);
            alert(result);
            // window.location.reload()
        })
        .catch((error) => {
            console.log("error", error);
            alert(result);
        });

}