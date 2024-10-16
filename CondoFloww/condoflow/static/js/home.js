// Exemplo de valores iniciais
let moradores = 75;
let totalFuncionarios = 15;
let funcionariosAtivos = 10;
let vagasRestantes = 25;
let totalVeiculos = 50

// Atualiza os valores na tela
function updateInfo() {
    document.getElementById('moradores').textContent = moradores;
    document.getElementById('totalFuncionarios').textContent = totalFuncionarios;
    document.getElementById('funcionariosAtivos').textContent = funcionariosAtivos;
    document.getElementById('vagasRestantes').textContent = vagasRestantes;
    document.getElementById('totalVeiculos').textContent = totalVeiculos;
}

updateInfo();