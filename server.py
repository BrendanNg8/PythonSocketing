import socket
import os
import platform

def shutdown_server():
    # Create TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5050))  # Listen on all interfaces
    server.listen(1)
    print("[SERVER LISTENING] on port 5050...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        
        # Receive shutdown command
        data = client_socket.recv(1024).decode("utf-8")
        if data.lower() == "shutdown":
            # Platform-specific shutdown commands
            if platform.system() == "Windows":
                os.system("shutdown /s /t 1")
            elif platform.system() in ["Linux", "Darwin"]:
                os.system("sudo shutdown -h now")
            client_socket.send("Shutdown initiated".encode("utf-8"))
            break
        client_socket.close()
    server.close()

shutdown_server()
