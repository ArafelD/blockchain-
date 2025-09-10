import hashlib
import json

def hash_data(data):
    """Gera o hash SHA256 de um dado."""
    data_string = json.dumps(data, sort_keys=True).encode('utf-8')
    return hashlib.sha256(data_string).hexdigest()


