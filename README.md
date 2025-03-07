# GeekPwnServer  

GeekPwnServer is a server-side program designed for security testing, automation, and penetration testing-related tasks.

## Features  
- Secure server-side scripting  
- Automated security analysis  
- Logging and request tracking  
- SQLite integration  

## Installation  

### 1. Clone the repository  
```bash
git clone https://github.com/your-username/GeekPwnServer.git
cd GeekPwnServer

### 2. Install dependencies

pip install -r requirements.txt

### **GeekPwnServer - Multi-Purpose Security Research & Penetration Testing Server**  

**Disclaimer:** This tool is for educational and ethical penetration testing purposes only. Unauthorized use is illegal.  

---

## **🛠 Requirements**
- Python 3.x  
- Pip installed  
- Required libraries (install with `pip install -r requirements.txt`)

### **📌 Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **🔥 Usage & Commands for Each Server**

### **1️⃣ HTTP Server (Payload Hosting)**
#### **Start HTTP Server on Port 8080**
```bash
python3 -m http.server 8080
```
📌 **Use Case:** Host payloads, exploits, or files for download.

---

### **2️⃣ Reverse Shell Listener**
#### **Start Listener on Port 4444**
```bash
python3 GeekPwnServer.py --reverse-shell 4444
```
📌 **Use Case:** Listen for incoming reverse shell connections.

---

### **3️⃣ Bind Shell Listener**
#### **Start Bind Shell on Port 5555**
```bash
python3 GeekPwnServer.py --bind-shell 5555
```
📌 **Use Case:** Attacker connects to an open bind shell on a compromised system.

---

### **4️⃣ Web Shell (Flask)**
#### **Start Web Shell on Port 8081**
```bash
python3 GeekPwnServer.py --web-shell
```
📌 **Use Case:** Execute system commands remotely via a web interface.

---

### **5️⃣ FTP Server**
#### **Start FTP Server**
```bash
python3 GeekPwnServer.py --ftp
```
📌 **Use Case:** File transfers and hosting.

---

### **6️⃣ SMB Server**
#### **Start SMB Server**
```bash
python3 GeekPwnServer.py --smb
```
📌 **Use Case:** Share files over a network (Windows/Linux).

---

### **7️⃣ DNS Tunnel Server**
#### **Start DNS Tunnel on Port 53**
```bash
python3 GeekPwnServer.py --dns
```
📌 **Use Case:** Data exfiltration via DNS tunneling.

---

### **8️⃣ TCP Shell (Netcat-like)**
#### **Start TCP Shell on Port 7777**
```bash
python3 GeekPwnServer.py --tcp 7777
```
📌 **Use Case:** Command execution via TCP.

---

## **📌 Example Use Cases & Real-World Scenarios**

1. **Penetration Testers:** Simulate attacks using bind/reverse shells.  
2. **Bug Bounty Hunters:** Host payloads for XSS, RCE, and LFI testing.  
3. **Red Teaming:** Bypass security defenses with DNS tunneling.  
4. **Networking & Protocol Testing:** Run custom servers to test security flaws.  
5. **Ethical Hacking Research:** Learn server exploitation methods.

---

## **🔧 Full Command Options**
```bash
python3 GeekPwnServer.py --help
```
This will display all available options and their usage.

---

