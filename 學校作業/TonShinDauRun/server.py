import socket
import threading

# 定義伺服器的 IP 位址和埠號
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5555

# 建立 TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 函數: 接收客戶端訊息並廣播給所有客戶端
def handle_client(client_socket, client_address):
    while True:
        try:
            # 接收客戶端的訊息
            message = client_socket.recv(1024).decode()
            if message:
                # 如果客戶端發送的是暱稱
                if client_address not in clients:
                    clients[client_address] = message
                    client_socket.send("Nickname set successfully".encode())
                else:
                    # 廣播訊息給所有客戶端
                    broadcast_message = f"{clients[client_address]}: {message}"
                    print(broadcast_message)
                    for client in clients:
                        client.send(broadcast_message.encode())
            else:
                # 如果沒有訊息，則中斷迴圈並移除該客戶端
                del clients[client_address]
                break
        except:
            # 如果發生錯誤，則中斷迴圈並移除該客戶端
            del clients[client_address]
            break

# 函數: 監聽成功提示
def listening_success():
    print(f"Server is listening on {SERVER_HOST}:{SERVER_PORT}")

# 啟動監聽成功提示的執行緒
listening_thread = threading.Thread(target=listening_success)
listening_thread.start()

# 綁定 IP 位址和埠號
server_socket.bind((SERVER_HOST, SERVER_PORT))

# 讓 socket 接受最多10個客戶端連線
server_socket.listen(10)

# 儲存已連線的客戶端和他們的暱稱
clients = {}

# 主迴圈: 接受新客戶端的連線
while True:
    client_socket, client_address = server_socket.accept()
    print(f"New connection from {client_address}")

    # 儲存客戶端連接
    clients[client_socket] = client_address

    # 建立一個新的執行緒來處理客戶端的訊息
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
