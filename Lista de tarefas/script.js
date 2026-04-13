const lista = document.getElementById('lista');

// 1. CARREGAR: Assim que a página abre, busca o que está salvo
window.onload = function() {
    const tarefasSalvas = JSON.parse(localStorage.getItem('minhasTarefas')) || [];
    tarefasSalvas.forEach(tarefaTexto => renderizarTarefa(tarefaTexto));
};

function adicionarTarefa() {
    let tarefaInput = document.getElementById('tarefa-input');
    let tarefaValor = tarefaInput.value;

    if (tarefaValor !== "") {
        renderizarTarefa(tarefaValor);
        salvarNoLocalStorage(); // Salva a nova lista
        tarefaInput.value = "";
    }
}

// Criamos essa função separada para não repetir código
function renderizarTarefa(texto) {
    let idUnico = 'item-' + Math.floor(Math.random() * 1000000);
    let novaTarefa = document.createElement('li');
    novaTarefa.setAttribute('id', idUnico);
    
    novaTarefa.innerHTML = `<span>${texto}</span>`;

    let deleteBtn = document.createElement('button');
    deleteBtn.classList.add('btn-delete');
    deleteBtn.innerHTML = 'Deletar';

    deleteBtn.onclick = function() {
        novaTarefa.remove();
        salvarNoLocalStorage(); // Salva após deletar
    };

    novaTarefa.appendChild(deleteBtn);
    lista.appendChild(novaTarefa);
}

// 2. SALVAR: Pega todos os textos das LIs e joga no LocalStorage
function salvarNoLocalStorage() {
    const todasAsTarefas = [];
    document.querySelectorAll('#lista li span').forEach(span => {
        todasAsTarefas.push(span.innerText);
    });
    
    // O LocalStorage só aceita Strings, por isso usamos o JSON.stringify
    localStorage.setItem('minhasTarefas', JSON.stringify(todasAsTarefas));
}