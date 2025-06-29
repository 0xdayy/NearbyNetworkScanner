#simple nearby network scanner
#so i read more about python learned imports etc and learned how to use tkinter to make a simple gui
#the program is of course open-source and you can use it to make an advanced and better versions!
#also enjoy my comments lmao
#DONT FORGET TO INSTALL THE REQUIREMENTS USING THE REQUIREMENTS.TXT FILE PLEASE DONT FORGOR!!!!


from scapy.all import ARP, Ether, srp  #here we are importing arp ether and srp from scappy (basically sum nerdy shi u dont care about)
import tkinter as tk  #here we importing tkinter so u see the fkin gui and not a damn terminal so yh ig cool
from tkinter import ttk  #more tkinter shi this getting boring but we goin to the juicy stuff


#OMG THE FUNCTION TO SCAN THE NETWORKS?!?!?!?
def scan_network():
    target_ip = entry_ip.get()
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []

    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    # we clearin the old treemap shi with this one so yh useful
    for i in tree.get_children():
        tree.delete(i)

    for device in devices:
        tree.insert("", "end", values=(device['ip'], device['mac']))

# FINALLY THE GUI U BEEN (NOT) WAITING FOR
root = tk.Tk()
root.title("Nearby Network Scanner 🛰️")
root.geometry("400x300")

label_ip = tk.Label(root, text="Target IP / Range:")
label_ip.pack()

entry_ip = tk.Entry(root)
entry_ip.insert(0, "192.168.1.1/24")  # example for yo dumb ahhh
entry_ip.pack()

scan_btn = tk.Button(root, text="Scan Network", command=scan_network)
scan_btn.pack()

tree = ttk.Treeview(root, columns=("IP", "MAC"), show='headings')
tree.heading("IP", text="IP Address")
tree.heading("MAC", text="MAC Address")
tree.pack(fill='both', expand=True)

root.mainloop()


#this the end bro nothing else. thanks if u read everythin u a real one. cya in my next project.