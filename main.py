from blockchain import Blockchain
from wallet import Wallet
from transaction import Transaction

# 1. Inicializando a Blockchain
print("\n--- 1. Inicializando a Blockchain ---")
my_blockchain = Blockchain()
print("Blockchain criada com o bloco gênese.")

# 2. Criando Carteiras
print("\n--- 2. Criando Carteiras ---")
wallet_a = Wallet()
wallet_b = Wallet()
wallet_miner = Wallet()
print(f"Carteira A (Endereço): {wallet_a.get_address()[:10]}...")
print(f"Carteira B (Endereço): {wallet_b.get_address()[:10]}...")
print(f"Carteira do Minerador (Endereço): {wallet_miner.get_address()[:10]}...")

# 3. Adicionando Transações Pendentes
print("\n--- 3. Adicionando Transações Pendentes ---")
my_blockchain.add_transaction(wallet_a.get_address(), wallet_b.get_address(), 10)
my_blockchain.add_transaction(wallet_b.get_address(), wallet_a.get_address(), 5)
print("Duas transações adicionadas à lista de pendentes.")

# 4. Minerando um Bloco
print("\n--- 4. Minerando um Bloco ---")
print(f"Minerador {wallet_miner.get_address()[:10]}... está minerando...")
mined_block = my_blockchain.mine_pending_transactions(wallet_miner.get_address())
print(f"Bloco minerado! Hash: {mined_block.hash[:10]}...")

# 5. Verificando Saldo
print("\n--- 5. Verificando Saldo ---")
# O minerador recebe a recompensa do bloco gênese e das transações pendentes
print(f"Saldo da Carteira do Minerador: {my_blockchain.get_balance_of_address(wallet_miner.get_address())}")
# Os saldos de A e B só serão atualizados após a mineração de blocos que contenham suas transações
print(f"Saldo da Carteira A: {my_blockchain.get_balance_of_address(wallet_a.get_address())}")
print(f"Saldo da Carteira B: {my_blockchain.get_balance_of_address(wallet_b.get_address())}")

# 6. Adicionando mais transações e minerando outro bloco
print("\n--- 6. Adicionando mais transações e minerando outro bloco ---")
my_blockchain.add_transaction(wallet_a.get_address(), wallet_miner.get_address(), 2)
my_blockchain.mine_pending_transactions(wallet_miner.get_address())
print(f"Saldo da Carteira do Minerador após segunda mineração: {my_blockchain.get_balance_of_address(wallet_miner.get_address())}")
print(f"Saldo da Carteira A após segunda transação: {my_blockchain.get_balance_of_address(wallet_a.get_address())}")

# 7. Verificando a validade da cadeia
print("\n--- 7. Verificando a validade da cadeia ---")
print(f"A Blockchain é válida? {my_blockchain.is_chain_valid()}")

# Exemplo de adulteração (para mostrar a segurança)
# my_blockchain.chain[1].transactions[0].amount = 1000000 # Tentar alterar uma transação
# print(f"A Blockchain é válida após adulteração? {my_blockchain.is_chain_valid()}")

# 8. Exibindo a Blockchain (simplificado)
print("\n--- 8. Exibindo a Blockchain (simplificado) ---")
for i, block in enumerate(my_blockchain.chain):
    print(f"\nBloco {i}:")
    print(f"  Hash: {block.hash}")
    print(f"  Hash Anterior: {block.previous_hash}")
    print(f"  Transações: {[t.to_dict() for t in block.transactions]}")
    print(f"  Timestamp: {block.timestamp}")
    print(f"  Nonce: {block.nonce}")


