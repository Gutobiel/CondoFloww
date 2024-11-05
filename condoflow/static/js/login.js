function logar() {
    var login = document.getElementById('login').value;
    var senha = document.getElementById('senha').value;

    if (login === "" || senha === "") {
        alert('Por favor, preencha todos os campos.');
        return false;
    } else {
        // Permitir que o formulário seja enviado
        return true;
    }
}