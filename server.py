import socket        #建立网络连接
import threading     #创建线程


clients = []

#通过服务器将客户端的话转给其他客户端
def broadcast(message_bytes,sender_socket):
    for client in clients[:]:      #clients[：]是clients的浅拷贝副本
        if client != sender_socket:
            try:
                client.sendall(message_bytes)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)
                    print(f"【系统】清理了一个掉线的客户端")


def handle_client(client_socket,client_address):
    """"这个函数会运行在子线程中，专门负责一个客户端"""
    clients.append(client_socket)

    welcome_msg = f"【系统】{client_address}加入了聊天室".encode('utf-8')
    broadcast(welcome_msg,client_socket)

    print(f"【服务员】{client_address}已记录在册,当前在线人数：{len(clients)}")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')    #decode将字节转换成字符串
            """一次可以接收1024个字节,剩余的留在内核里的接收缓冲区下次再取"""
            if not message:
                print(f"【服务员】{client_address}主动断开了")
                break

            print(f"[{client_address}说{message}]")
            broadcast_message = f"[{client_address}]{message}".encode('utf-8')
            broadcast(broadcast_message,client_socket)

        except Exception as e:
            print(f"【服务员】{client_address}异常断开了：{e}")
            break

    client_socket.close()#?

    leave_msg = f"【系统】{client_address}离开了聊天室".encode('utf-8')
    broadcast(leave_msg,client_socket)

    print(f"【服务员】{client_address}的服务已结束，当前在线人数：{len(clients)}")


server_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
""""创建了一个IPv4 (AF_INET) 的TCP (SOCK_STREAM) Socket"""

server_socket.bind(('0.0.0.0',8888))
""""bind() 将这个Socket绑定到一个固定的IP地址和端口号"""
"""'0.0.0.0' 表示监听本机所有网络接口(包括127.0.0.1和局域网IP),这样局域网内任何设备都能连接"""

server_socket.listen(5)
print("服务器已启动，等待连接……")

while True:
    client_socket,client_address = server_socket.accept()#?
    print(f"【老板】新客人来了{client_address}")

    client_thread = threading.Thread(target = handle_client,args = (client_socket,client_address))
    """"创建一个新的线程,目标函数是handle_client,并把新Socket(accept()返回)和地址传给它"""
    client_thread.start()

    print(f"【老板】已派服务员给{client_address}，继续等待")
