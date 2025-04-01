from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connessione da {addr}")

    # Riceve la stringa dal client
    sentence = connectionSocket.recv(1024).decode()
    
    # Controlla se è un palindromo con if e restituisce un valore booleano
    if sentence == sentence[::-1]:
        is_palindrome = True
    else:
        is_palindrome = False

    # Invia il valore booleano al client
    connectionSocket.send(str(is_palindrome).encode())  # Convertito in stringa per l'invio perché con il socket si possono inviare solo interi o stringhe

    connectionSocket.close()
