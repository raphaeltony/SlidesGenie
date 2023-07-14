var submitButton = document.getElementById("submitButton")
submitButton.addEventListener("click", get_loader);

function get_loader() {
    console.log("work");
    var pgbar = document.querySelector('#progress')

    pgbar.classList.toggle('d-none')
}