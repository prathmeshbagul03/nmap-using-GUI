import tkinter as tk
from tkinter import messagebox
import os

# Function to run the selected scan
def run_scan():
    target = target_entry.get()
    choice = scan_type.get()

    if not target:
        messagebox.showerror("Error", "Please enter a target!")
        return

    commands = {
        1: f"nmap -sn {target}",
        2: f"nmap -sS {target}",
        3: f"nmap -sT {target}",
        4: f"nmap -sU {target}",
        5: f"nmap -O {target}",
        6: f"nmap -sV {target}",
        7: f"nmap -A {target}",
        8: f"nmap -p- {target}",
        9: f"nmap {custom_entry.get()} {target}"
    }

    if choice in commands:
        os.system(commands[choice])
        messagebox.showinfo("Scan Complete", "The scan has finished!")
    else:
        messagebox.showerror("Error", "Invalid scan type selected!")

# Create the main window
root = tk.Tk()
root.title("Nmap Easy Interface")

# Target input
tk.Label(root, text="Enter Target IP or Hostname:").grid(row=0, column=0)
target_entry = tk.Entry(root)
target_entry.grid(row=0, column=1)

# Scan type selection
tk.Label(root, text="Select Scan Type:").grid(row=1, column=0)
scan_type = tk.IntVar()
scan_options = [
    ("Ping Scan", 1),
    ("TCP SYN Scan", 2),
    ("TCP Connect Scan", 3),
    ("UDP Scan", 4),
    ("OS Detection", 5),
    ("Version Detection", 6),
    ("Aggressive Scan", 7),
    ("Full Scan", 8),
    ("Custom Scan", 9)
]
for i, (text, val) in enumerate(scan_options):
    tk.Radiobutton(root, text=text, variable=scan_type, value=val).grid(row=i+2, column=0, sticky="w")

# Custom scan input
tk.Label(root, text="Custom Nmap Options:").grid(row=11, column=0)
custom_entry = tk.Entry(root)
custom_entry.grid(row=11, column=1)

# Run button
tk.Button(root, text="Run Scan", command=run_scan).grid(row=12, column=0, columnspan=2)

# Start the GUI
root.mainloop()
