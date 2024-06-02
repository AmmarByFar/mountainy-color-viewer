import csv
import tkinter as tk
from tkinter import ttk
import pyperclip

def copy_hex_code(hex_code):
    pyperclip.copy(hex_code)

def copy_sku(sku):
    pyperclip.copy(sku)

# Create the main window
window = tk.Tk()
window.title("Color Catalog")

# Create a frame to hold the Treeview and scrollbar
frame = ttk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True)

# Create a Treeview widget
tree = ttk.Treeview(frame, columns=("Name", "Hex", "Size", "SKU", "Color"), show="headings")
tree.heading("Name", text="Color Name")
tree.heading("Hex", text="Hex Code")
tree.heading("Size", text="Size")
tree.heading("SKU", text="SKU")
tree.heading("Color", text="Color")

tree.column("Name", width=200)
tree.column("Hex", width=100)
tree.column("Size", width=100)  # Use tree.column() instead of tree.heading()
tree.column("SKU", width=100)
tree.column("Color", width=50)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Treeview to use the scrollbar
tree.configure(yscrollcommand=scrollbar.set)

# Read the CSV file
with open('bc3001-skus.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        color_name = row['Color']
        hex_code = row['HexCode']
        size = row['Size']  # Extract the size value from the CSV row
        sku = row['SKU']

        # Insert the color data into the Treeview
        tree.insert("", tk.END, values=(color_name, hex_code, size, sku, ""), tags=(hex_code,))

        # Configure the color box for each row
        tree.tag_configure(hex_code, background=hex_code)

# Create a right-click context menu for copying the hex code and SKU
def show_context_menu(event):
    item = tree.identify_row(event.y)
    if item:
        tree.selection_set(item)
        hex_code = tree.item(item, "values")[1]
        sku = tree.item(item, "values")[3]  # Update the index to retrieve the SKU value
        context_menu.entryconfigure("Copy Hex Code", command=lambda: copy_hex_code(hex_code))
        context_menu.entryconfigure("Copy SKU", command=lambda: copy_sku(sku))
        context_menu.post(event.x_root, event.y_root)

context_menu = tk.Menu(window, tearoff=0)
context_menu.add_command(label="Copy Hex Code")
context_menu.add_command(label="Copy SKU")

tree.bind("<Button-3>", show_context_menu)

# Start the Tkinter event loop
window.mainloop()