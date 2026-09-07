import socket
import threading


def receive_message(client_socket):
    while True:
        try:
            message_bytes = client_socket.recv(1024)

            if not message_bytes:
                print("\n【系统】服务器已关闭连接")
                break

            message = message_bytes.decode('utf-8')
            print(f"\n{message}")
            print("> ",end="",flush=True)
            """print 默认会在末尾加换行，改成 end="" 表示不换行"""
            """flush=True 表示立即刷新屏幕，让 > 立刻显示出来"""

        except Exception as e:
            print(f"\n【系统】接收消息时出错:{e}")
            break

    client_socket.close()
    print("【系统】已断开与服务器的连接")
 

def start_client(server_ip = '127.0.0.1',server_port = 8888):
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client_socket.connect((server_ip,server_port))
        print(f"【系统】成功连接到服务器{server_ip,server_port}")
        print("提示：输入消息并按回车发送，输入/quit退出")
        print("> ",end="",flush=True)
        
    except Exception as e:
        print(f"【错误】无法连接到服务器：{e}")
        return

    receive_thread = threading.Thread(target = receive_message,args=(client_socket,))
    receive_thread.daemon = True     #主线程结束，子线程会强制终止
    receive_thread.start()
    print("【系统】接收线程已启动，开始监听服务器消息")


    while True:
        try:
            message = input("> ")

            #输入/quit，退出循环
            if message.lower() == '/quit':
                print("【系统】正在退出……")
                break

            #不发送空消息
            if not message.strip():
                print("> ",end="",flush=True)
                continue

            client_socket.sendall((message).encode('utf-8'))

        except Exception as e:
            print(f"【错误】发送消息失败：{e}")
            break

    client_socket.close()
    print("【系统】已退出聊天室")


if __name__ == "__main__":
    server_ip = input("请输入服务器IP地址：")
    print(f"正在连接{server_ip}")
    start_client(server_ip)