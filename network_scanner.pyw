import tkinter as tk
from tkinter import messagebox
import scapy.all as scapy

def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    devices = []
    for element in answered_list:
        device = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        devices.append(device)
    
    return devices

def display_devices():
    ip_range = entry.get()
    if not ip_range:
        messagebox.showerror("Error", "Please enter the IP range to scan.")
        return
    
    devices = scan_network(ip_range)
    if not devices:
        messagebox.showinfo("Scan Results", "No devices found on the network.")
        return
    
    result = "Devices connected to the network:\n"
    for device in devices:
        result += f"IP: {device['IP']}, MAC: {device['MAC']}\n"
    
    messagebox.showinfo("Scan Results", result)


root = tk.Tk()
root.title("Network Scanner")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - 400) / 2
y_coordinate = (screen_height - 200) / 2


root.geometry("400x200+{}+{}".format(int(x_coordinate), int(y_coordinate)))

label = tk.Label(root, text="Enter IP range (e.g., 192.168.1.1/24):")
label.pack()

entry = tk.Entry(root)
entry.pack()

scan_button = tk.Button(root, text="Scan Network", command=display_devices)
scan_button.pack()

root.mainloop()
