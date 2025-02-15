document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("buscarForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Evita recarregar a página

        let nomeTravessa = document.getElementById("nome_travessa").value;

        fetch("/buscar", {  
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams({ nome_travessa: nomeTravessa })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Resposta do servidor:", data); // Para debug

            let resultadoDiv = document.getElementById("resultado");
            resultadoDiv.innerHTML = "";

            if (data.resultados && Array.isArray(data.resultados)) {
                data.resultados.forEach(item => {
                    resultadoDiv.innerHTML += `
                        <div class="resultado-item">
                            <div class="nome-travessa">${item.nome}</div>
                            <div class="endereco-travessa">${item.endereco}</div>
                        </div>
                    `;
                });
            } else {
                resultadoDiv.innerHTML = `<div class="sem-resultados">🔍 Nenhum resultado encontrado</div>`;
            }
        })
        .catch(error => {
            console.error("Erro na requisição:", error);
            document.getElementById("resultado").innerHTML = `<div class="sem-resultados">❌ Erro ao buscar dados</div>`;
        });
    });
});
