import socket
import threading

# 定義伺服器的 IP 位址和埠號
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5555

# 建立 TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 連接至伺服器
client_socket.connect((SERVER_HOST, SERVER_PORT))

# 函數: 接收伺服器訊息並顯示
def receive_message():
    while True:
        try:
            # 接收伺服器訊息
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            # 如果發生錯誤，表示與伺服器斷開連接
            print("Disconnected from server.")
            client_socket.close()
            break

# 函數: 輸入暱稱
def input_nickname():
    nickname = input("Enter your nickname: ")
    client_socket.send(nickname.encode())

    # 確認暱稱是否成功傳送到伺服器
    confirmation = client_socket.recv(1024).decode()
    if confirmation == "Nickname set successfully":
        print("Nickname set successfully")
        # 啟動接收訊息的執行緒
        receive_thread.start()
    else:
        print("Failed to set nickname")

# 函數: 發送訊息
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode())

# 啟動接收訊息的執行緒
receive_thread = threading.Thread(target=receive_message)

# 輸入暱稱
input_nickname()

# 啟動發送訊息的執行緒
send_thread = threading.Thread(target=send_message)
send_thread.start()
