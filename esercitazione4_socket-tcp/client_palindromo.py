from socket import *

serverName = 'localhost'  # Cambia con l'IP del server se in rete
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Inserimento della stringa da verificare
sentence = input('Inserisci una stringa per verificare se è un palindromo: ')
clientSocket.send(sentence.encode())

# Ricezione del risultato dal server e conversione in booleano
response = clientSocket.recv(1024).decode()
# Convertire la stringa ricevuta in booleano
if response == "True":
    is_palindrome = True
else:
    is_palindrome = False

print(f"Il server dice: {is_palindrome}")

clientSocket.close()