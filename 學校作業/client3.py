import socket
import threading

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
        except:
            # If there's an error receiving messages, exit the loop
            break

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('26.36.225.162', 5555)
client_socket.connect(server_address)

# Ask for nickname
nickname = input("Enter your nickname: ")
# Display the nickname locally
print("You are now chatting as:", nickname + ":")

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main loop to send messages to the server
while True:
    message = input()
    if message.lower() == 'exit':
        break
    # Send the message to the server with nickname
    client_socket.send((nickname + ": " + message).encode('utf-8'))

# Close the client socket
client_socket.close()
