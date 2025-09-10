[README.md](https://github.com/user-attachments/files/22251157/README.md)
# Projeto de Demonstração de Blockchain em Python

Este projeto simples em Python demonstra os conceitos fundamentais de uma blockchain, incluindo a criação de blocos, transações, mineração (simplificada) e verificação da cadeia.

## Estrutura do Projeto

```
blockchain_project/
├── main.py
├── blockchain.py
├── block.py
├── transaction.py
├── wallet.py
├── utils.py
├── requirements.txt
└── README.md
```

*   `main.py`: O ponto de entrada da aplicação, onde a blockchain é inicializada, transações são adicionadas, blocos são minerados e saldos são verificados.
*   `blockchain.py`: Define a classe `Blockchain`, que gerencia a cadeia de blocos, transações pendentes e a lógica de mineração.
*   `block.py`: Define a classe `Block`, representando um bloco individual na cadeia, contendo transações, timestamp, hash do bloco anterior e seu próprio hash.
*   `transaction.py`: Define a classe `Transaction`, que representa uma transação entre duas partes.
*   `wallet.py`: Simula uma carteira de criptomoedas, gerando chaves públicas/privadas e permitindo a assinatura de transações.
*   `utils.py`: Contém funções utilitárias, como a função de hashing.
*   `requirements.txt`: Lista as dependências do projeto.

## Como Executar

1.  **Navegue até o diretório do projeto:**
    ```bash
    cd blockchain_project
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute o script principal:**
    ```bash
    python3 main.py
    ```

## Exemplos Práticos e Aplicações Reais (Demonstradas no `main.py`)

O script `main.py` simula um cenário básico de blockchain, onde:

*   **Inicialização da Blockchain:** Uma nova blockchain é criada com um bloco gênese.
*   **Criação de Carteiras:** Múltiplas carteiras são geradas para simular usuários e um minerador.
*   **Adição de Transações:** Transações são criadas e adicionadas à lista de transações pendentes.
*   **Mineração de Blocos:** Um minerador processa as transações pendentes, cria um novo bloco e o adiciona à cadeia. O minerador recebe uma recompensa por seu trabalho.
*   **Verificação de Saldo:** Os saldos das carteiras são atualizados e verificados após as transações e mineração.
*   **Validação da Cadeia:** A integridade da blockchain é verificada para garantir que nenhum bloco foi adulterado.

Este projeto serve como uma base para entender como as blockchains funcionam em um nível fundamental. A partir daqui, você pode explorar conceitos mais avançados como Proof of Stake, contratos inteligentes, redes de teste e muito mais!

