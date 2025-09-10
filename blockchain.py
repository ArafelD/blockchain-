import time
from block import Block
from transaction import Transaction
from utils import hash_data

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        self.pending_transactions.append(transaction)
        return self.get_last_block().index + 1

    def mine_pending_transactions(self, mining_reward_address):
        block = Block(len(self.chain), self.pending_transactions, time.time(), self.get_last_block().hash)
        
        # Simple Proof of Work (for demonstration purposes)
        # In a real blockchain, this would be a more complex mining process
        block.hash = block.calculate_hash()
        
        self.chain.append(block)
        self.pending_transactions = [
            Transaction("network", mining_reward_address, 1) # Mining reward
        ]
        return block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def get_balance_of_address(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.sender == address:
                    balance -= transaction.amount
                if transaction.recipient == address:
                    balance += transaction.amount
        return balance


