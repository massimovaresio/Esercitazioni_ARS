from socket import *

serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connessione da {addr}")

    # Ricevi il primo numero e convertilo in int (rimuovi il carattere di fine riga '\n')
    num1 = int(connectionSocket.recv(1024).decode())

    # Ricevi il secondo numero e convertilo in int (rimuovi il carattere di fine riga '\n')
    num2 = int(connectionSocket.recv(1024).decode())

    # Ricevi l'operazione da eseguire (rimuovi il carattere di fine riga '\n')
    operation = connectionSocket.recv(1024).decode()

    # Calcola il risultato in base all'operazione
    if operation == "somma":
        result = num1 + num2
    elif operation == "sottrazione":
        result = num1 - num2
    elif operation == "moltiplicazione":
        result = num1 * num2
    elif operation == "divisione":
        # Gestisci la divisione con attenzione per evitare divisione per zero
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Errore: divisione per zero"
    else:
        result = "Operazione non valida"

    # Invia il risultato al client
    connectionSocket.send(str(result).encode())

    connectionSocket.close()

