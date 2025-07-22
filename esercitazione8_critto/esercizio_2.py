from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

# Dati forniti
nonce = b"CiaoCiao" # Nonce di 8 bytes (64 bit)
key = b"questa chiave e' proprio sicura!" # Chiave di 32 bytes (256 bit)
ciphertext_b64 = b'OKx7Cl067lFWiqYMS4zmMNfzbrsrEo4Dhgt96srvQm+ohg=='
ciphertext = b64decode(ciphertext_b64) # Testo cifrato in formato binario

# 1. Crea un oggetto cifrario ChaCha20 per la decifratura
# Per decifrare, usi la stessa chiave e lo stesso nonce che sono stati usati per cifrare.
cipher = ChaCha20.new(key=key, nonce=nonce)

# 2. Decifra il ciphertext
# Il metodo decrypt funziona sia per cifrare che per decifrare nei cifrari a flusso
plaintext_bytes = cipher.decrypt(ciphertext)

# 3. Decodifica il messaggio originale da bytes a stringa leggibile (se era testo)
original_message = plaintext_bytes.decode('utf-8')

print(f"Nonce utilizzato: {nonce.hex()}")
print(f"Chiave utilizzata: {key.hex()}")
print(f"Testo cifrato (Base64): {ciphertext_b64.decode()}")
print(f"Messaggio originale decifrato: {original_message}")