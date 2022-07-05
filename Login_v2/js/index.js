var btn = document.getElementsByClassName("login100-form-btn");
btn.addeventListener("c
lick", function(e){
    e.preventDefault();
    const email = document.querySelector(".email");
    const pass =  document.querySelector(".pass");
    const emaill = email.value;
    const passs = pass.value;
    if (emaill === "bolivarartur77@gmail.com" && passs === 56916050){
        console.log("senha correta")
        
    }
    else{
        console.log("senha incorreta")
    }

})