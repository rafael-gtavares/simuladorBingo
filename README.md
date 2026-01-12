# Simulador de Bingo Acadêmico 🎰

Projeto desenvolvido em outubro de 2025 como parte de um trabalho acadêmico. A aplicação consiste em uma simulação completa de um jogo de bingo, desde a geração automatizada de cartelas únicas até a verificação dinâmica de vencedores.

## 👥 Equipe de Desenvolvimento
Este projeto foi construído em colaboração com:
* [Caio Honório](LINK_GITHUB_OU_LINKEDIN)
* [Davi Honório](LINK_GITHUB_OU_LINKEDIN)
* [Guilherme Duarte](LINK_GITHUB_OU_LINKEDIN)
* [Rafael Tavares] (Eu)
* [Victor Lessa](LINK_GITHUB_OU_LINKEDIN)

## 🛠️ Funcionalidades
* **Geração de Cartelas:** Criação de 100 cartelas únicas (matrizes 5x5) com números aleatórios de 0 a 99, garantindo que não existam números repetidos na mesma cartela nem cartelas idênticas no sistema.
* **Sorteio Inteligente:** Sorteio de números sem repetição até que uma cartela seja completada.
* **Verificação em Tempo Real:** * Identificação do primeiro vencedor de **linha**.
    * Identificação do primeiro vencedor de **coluna**.
    * Encerramento automático ao atingir o **Bingo** (cartela completa).

## 🚀 Tecnologias e Conceitos Aplicados
* **Linguagem:** Python
* **Lógica de Matrizes:** Manipulação de listas aninhadas para representar as cartelas.
* **Algoritmos de Busca:** Verificação constante de números sorteados dentro das matrizes.
* **Controle de Fluxo:** Uso avançado de loops `while` e `for`, além de condicionais complexas.

## 📂 Como executar
1. Certifique-se de ter o Python instalado.
2. Execute o arquivo principal:
   ```bash
   python nome_do_arquivo.py
