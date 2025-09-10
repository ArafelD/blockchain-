import hashlib
import json
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class Wallet:
    def __init__(self):
        self.private_key = RSA.generate(2048)
        self.public_key = self.private_key.publickey()
        self.address = self.public_key.export_key().decode("utf-8")

    def sign_transaction(self, transaction):
        h = SHA256.new(json.dumps(transaction.to_dict(), sort_keys=True).encode("utf-8"))
        signature = pkcs1_15.new(self.private_key).sign(h)
        return signature.hex()

    def get_public_key(self):
        return self.public_key.export_key().decode("utf-8")

    def get_address(self):
        return self.address

    @staticmethod
    def verify_signature(public_key, transaction, signature):
        public_key_obj = RSA.import_key(public_key.encode("utf-8"))
        h = SHA256.new(json.dumps(transaction.to_dict(), sort_keys=True).encode("utf-8"))
        try:
            pkcs1_15.new(public_key_obj).verify(h, bytes.fromhex(signature))
            return True
        except (ValueError, TypeError):
            return False


