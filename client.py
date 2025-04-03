import socket

def trigger_shutdown(server_ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((server_ip, 5050))
        client.send("shutdown".encode("utf-8"))
        response = client.recv(1024).decode("utf-8")
        print(response)
    finally:
        client.close()

# Replace with target machine's IP
trigger_shutdown("192.168.1.100")



