# import lib
from Crypto.Hash import SHA256

FILENAME = "test_file.txt"

hash_object = SHA256.new() # Inizializza l'oggetto hash SHA256

with open(FILENAME, "rb") as f_input:
    file_content = f_input.read()

hash_object.update(file_content)

hash_digest = hash_object.hexdigest()

print(f"L'hash SHA256 è: {hash_digest}")