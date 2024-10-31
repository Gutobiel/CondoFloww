<<<<<<< HEAD
function logar(){

    var login = document.getElementById('login').value;
    var senha = document.getElementById('senha').value;

    if(login == "admin" && senha == "admin"){
        alert('Sucesso');
        location.href = "/templates/core/home.html";
    }else{
        alert('Usuário ou senha incorretos');
    }
}
=======
function logar(){

    var login = document.getElementById('login').value;
    var senha = document.getElementById('senha').value;

    if(login == "admin" && senha == "admin"){
        alert('Sucesso');
        location.href = "/templates/core/home.html";
    }else{
        alert('Usuário ou senha incorretos');
    }
}
>>>>>>> 18f907a56d8691b27eea50f6cf9e9d105f9e4784
