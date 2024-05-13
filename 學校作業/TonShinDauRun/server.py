import socket
import threading

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"Connected to {address}")
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Received message from {address}: {data}")
        # Call broadcast function, passing the client's socket as an argument
        broadcast(data, client_socket)

    print(f"Connection from {address} closed.")
    client_socket.close()

# Function to broadcast message to all clients
def broadcast(message, sender_socket):
    if clients:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    # Remove the client if it's not responsive
                    clients.remove(client)


# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('26.36.225.162', 5555)

# Bind the server to the address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening...")

# List to keep track of connected clients
clients = []

# Main loop to accept incoming connections
while True:
    # Accept a new connection
    client_socket, address = server_socket.accept()
    clients.append(client_socket)

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
