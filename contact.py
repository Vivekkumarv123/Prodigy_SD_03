import tkinter as tk
from tkinter import messagebox, font
import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    
    if not name or not phone or not email:
        messagebox.showerror("Input Error", "All fields are required.")
        return
    
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    update_contact_list()
    clear_entries()

# Update contact list display
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact["name"])

# Show contact details when selected
def show_contact_details(event):
    selected_index = contact_list.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact["name"])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact["phone"])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact["email"])

# Edit selected contact
def edit_contact():
    selected_index = contact_list.curselection()
    if not selected_index:
        messagebox.showerror("Selection Error", "Select a contact to edit.")
        return
    
    contacts[selected_index[0]] = {
        "name": entry_name.get(),
        "phone": entry_phone.get(),
        "email": entry_email.get()
    }
    save_contacts(contacts)
    update_contact_list()
    clear_entries()

# Delete selected contact
def delete_contact():
    selected_index = contact_list.curselection()
    if not selected_index:
        messagebox.showerror("Selection Error", "Select a contact to delete.")
        return
    
    contacts.pop(selected_index[0])
    save_contacts(contacts)
    update_contact_list()
    clear_entries()

# Clear input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("700x600")
root.configure(bg='#ecf0f1')

# Custom font
custom_font = font.Font(family="Helvetica", size=12)

# Load contacts
contacts = load_contacts()

# UI elements
frame = tk.Frame(root, bg='#ecf0f1')
frame.pack(pady=20)

label_name = tk.Label(frame, text="Name:", bg='#ecf0f1', font=custom_font)
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_name = tk.Entry(frame, width=30, font=custom_font)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_phone = tk.Label(frame, text="Phone:", bg='#ecf0f1', font=custom_font)
label_phone.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_phone = tk.Entry(frame, width=30, font=custom_font)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(frame, text="Email:", bg='#ecf0f1', font=custom_font)
label_email.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_email = tk.Entry(frame, width=30, font=custom_font)
entry_email.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(frame, text="Add Contact", command=add_contact, bg='#2ecc71', fg='white', width=15, font=custom_font)
add_button.grid(row=3, column=0, padx=10, pady=10)

edit_button = tk.Button(frame, text="Edit Contact", command=edit_contact, bg='#f39c12', fg='white', width=15, font=custom_font)
edit_button.grid(row=3, column=1, padx=10, pady=10)

delete_button = tk.Button(frame, text="Delete Contact", command=delete_contact, bg='#e74c3c', fg='white', width=15, font=custom_font)
delete_button.grid(row=4, column=0, padx=10, pady=10)

clear_button = tk.Button(frame, text="Clear", command=clear_entries, bg='#3498db', fg='white', width=15, font=custom_font)
clear_button.grid(row=4, column=1, padx=10, pady=10)

contact_list = tk.Listbox(root, height=15, width=50, font=custom_font)
contact_list.pack(pady=20)
contact_list.bind('<<ListboxSelect>>', show_contact_details)

# Populate the listbox with contacts
update_contact_list()

# Run the main loop
root.mainloop()
