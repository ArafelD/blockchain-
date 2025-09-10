import time
from utils import hash_data

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.transactions) + str(self.timestamp) + str(self.previous_hash) + str(self.nonce)
        return hash_data(block_string)

    def to_dict(self):
        return {
            'index': self.index,
            'transactions': [t.to_dict() for t in self.transactions],
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'hash': self.hash
        }


