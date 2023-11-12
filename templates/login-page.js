const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "NamanJangid" && password === "Naman") {
        //alert("You have successfully logged in.");
		window.open("main-page.html")
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
		setTimeout(function(){
        location.reload();},2000);
    }
})