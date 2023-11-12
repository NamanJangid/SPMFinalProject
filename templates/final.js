const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.AccessToken.value;
    //const password = loginForm.password.value;

    if (username === "grc-iit/coeus-adapter") {
        //alert("You have successfully logged in.");
		window.open("https://airtable.com/appCy4sKiyIq7HeiL/pagvZ9PbBWdxIb40F")
        location.reload();
    } else {
        window.open("https://airtable.com/invite/l?inviteId=inv5Pp4pM9xictPE9&inviteToken=a1cd53c37bb45c26a650e16d017d076d24351c7b6ed367f308c50de5c01ce04b&utm_medium=email&utm_source=product_team&utm_content=transactional-alerts")
        location.reload();
    }
})