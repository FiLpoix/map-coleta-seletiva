async function adicionarPonto() {
    const nome = document.getElementById('nome').value;
    const descricao = document.getElementById('descricao').value;
    const endereco = document.getElementById('endereco').value;
    const latitude = parseFloat(document.getElementById('latitude').value);
    const longitude = parseFloat(document.getElementById('longitude').value);

    const response = await fetch('/api/pontos/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nome, descricao, endereco, latitude, longitude }),
    });

    const messageDiv = document.getElementById('message');
    if (response.ok) {
        messageDiv.style.color = 'green';
        messageDiv.textContent = 'Ponto de coleta adicionado com sucesso!';
        document.getElementById('pontoForm').reset();
    } else {
        messageDiv.style.color = 'red';
        messageDiv.textContent = 'Erro ao adicionar o ponto de coleta. Tente novamente.';
    }
}