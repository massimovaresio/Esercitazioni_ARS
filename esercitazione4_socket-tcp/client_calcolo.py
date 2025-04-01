import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Chiedi all'utente di inserire i due numeri
num1 = int(input("Inserisci il primo numero: "))  # Inserimento primo numero
num2 = int(input("Inserisci il secondo numero: "))  # Inserimento secondo numero

# Invia il primo numero (convertito in stringa)
client_socket.send((str(num1)).encode())

# Invia il secondo numero (convertito in stringa)
client_socket.send((str(num2)).encode())

# Chiedi all'utente di scegliere l'operazione
operation = input("Inserisci l'operazione (somma, sottrazione, moltiplicazione, divisione): ").lower()

# Invia l'operazione (già stringa) con un carattere di fine
client_socket.send((operation).encode())

# Ricevi il risultato dal server
response = client_socket.recv(1024)
print("Risultato dal server:", response.decode())

client_socket.close()