var submitButton = document.getElementById("submitButton")
submitButton.addEventListener("click", submit_request);

function update_pgbar(perc){
    var pgbar = document.querySelector('#progress-bar');
    pgbar.style.width = `${perc}%`
}

function submit_request() {
    console.log("work");
    var pgbar = document.querySelector('#progress')
    var currentPage = window.location.href.split('/').slice(-1)

    pgbar.classList.toggle('d-none')

    setTimeout(update_pgbar,20000,25)  //20 secs
    setTimeout(update_pgbar,90000,50)  // 1.5 min
    setTimeout(update_pgbar,150000,80) // 2.5 min
    setTimeout(update_pgbar,210000,100) // 3.5


    event.preventDefault()
    const userInput = document.getElementById("message").value;
    let styleSelect = "";
    let llm = "";   
    let imageModel= "";

    if(currentPage=='slidesgenie')
        styleSelect = document.querySelector('input[name="styleSelect"]:checked').value;

    if(currentPage=='memorylane' || currentPage=='uploader'){
        llm = document.querySelector('input[name="llm"]:checked').value;
        imageModel = document.querySelector('input[name="imageModel"]:checked').value;
    }
    // console.log(eventname,instname,startdate,enddate,prize,level,cashprize)

    var formdata = new FormData();
    formdata.append("userInput", userInput);
    if(currentPage=='slidesgenie')
        formdata.append("styleSelect", styleSelect);

    if(currentPage=='memorylane'|| currentPage=='uploader'){
        formdata.append("llm", llm);
        formdata.append("imageModel",imageModel);
    }
    
    var requestOptions = {
        method: "POST",
        body: formdata,
        redirect: "follow"
    };

    fetch("/submit/", requestOptions)
        .then((response) => response.text())
        .then((result) => {
            console.log(result);
            // alert(result);
            location.href = result
        })
        .catch((error) => {
            console.log("error", error);
            alert(result);
        });

}