from tkinter import *
import socket as sc
from colorama import Fore

root = Tk()
root.title("Port Scanner")
root.geometry("495x185")
root.resizable(False, False)
root.configure(background="black")

# Function
def scan (target, ports):
    for port in range (1, ports):
        scan_port(target, port)

def scan_port(alamatIP, port):
    try:
        sock = sc.socket()
        sock.connect((alamatIP, port))
        print("[+] Port "+str(port)+" Terbuka")
        sock.close()
    except:
        print("[-] Port "+str(port)+" Tertutup")


def start_scan():
    if ',' in entry_target.get():
        print("[*] Scan Beberapa Target")
        for ip_addr in entry_target.get().split(','):
            scan(ip_addr.strip(' '), int(entry_port.get()))
    else:
        scan(entry_target.get(), int(entry_port.get()))

# Widgets
label_target = Label(root, text="Masukkan IP Targets : ", fg="#00FF00", bg="black")
label_target.grid(row=1, column=1, padx=5, pady=5)

entry_target = Entry(root, width=30, justify=CENTER, fg="white", bg="#808080")
entry_target.grid(row=2, column=1, padx=5, pady=5)

label_port = Label(root, text="Jumlah Port Scan : ", fg="#00FF00", bg="black")
label_port.grid(row=3, column=1, padx=5, pady=5)

entry_port = Entry(root, width=30, justify=CENTER, fg="white", bg="#808080")
entry_port.grid(row=4, column=1, padx=5, pady=5)

scan_btn = Button(root, text="SCAN!!", width=10, command=start_scan, fg="#00FF00", bg="black")
scan_btn.grid(row=5, column=1, padx=10, pady=10)

label_kata = Label(root, text="PBL-RKS | POLITEKNIK NEGERI BATAM", font=("Capsula", "5"),fg="white", bg="black", justify=RIGHT)
label_kata.grid(row=6, column=0, padx=5, pady=5)

root.mainloop()