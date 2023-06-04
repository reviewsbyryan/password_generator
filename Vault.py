import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import json
import os


class PasswordGenerator:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Widgets
        self.master_password_entry = tk.Entry(root, show="*")
        self.salt_entry = tk.Entry(root)
        self.password_entry = tk.Entry(root, show="*", width=40)
        self.generate_button = tk.Button(root, text="Generate", command=self.generate_password)
        self.save_button = tk.Button(root, text="Save", command=self.save_password)
        self.copy_button = tk.Button(root, text="Copy", command=self.copy_password)

        # Grid configuration
        for i in range(2):
            root.grid_columnconfigure(i, weight=1)
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)

        # Padding
        padding = {"padx": 10, "pady": 10}
        
        # Widgets placement with padding
        tk.Label(root, text="Master Password:").grid(row=0, column=0, sticky='EW', **padding)
        tk.Label(root, text="Metadata:").grid(row=1, column=0, sticky='EW', **padding)
        self.master_password_entry.grid(row=0, column=1, sticky='EW', **padding)
        self.salt_entry.grid(row=1, column=1, sticky='EW', **padding)
        self.generate_button.grid(row=2, column=0, columnspan=2, sticky='EW', **padding)
        self.password_entry.grid(row=3, column=0, columnspan=2, sticky='EW', **padding)
        self.save_button.grid(row=4, column=0, sticky='EW', **padding)
        self.copy_button.grid(row=4, column=1, sticky='EW', **padding)

    def generate_password(self):
        master_password = self.master_password_entry.get()
        salt = self.salt_entry.get()

        salt = salt.encode()  # Convert to bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(master_password.encode())  # Can only use kdf once
        password = base64.urlsafe_b64encode(key).decode()  # Convert to string and remove '=' padding
        self.password_entry.delete(0, 'end')  # Clear existing password
        self.password_entry.insert(0, password.rstrip("="))  # Insert new password

    def save_password(self):
        answer = messagebox.askyesno("Confirmation", "Are you sure you want to save this password?")
        if answer:
            password = self.password_entry.get()
            password = password.encode()

            # Generate key
            key = base64.urlsafe_b64encode(os.urandom(32))
            cipher_suite = Fernet(key)

            # Encrypt password
            cipher_text = cipher_suite.encrypt(password)

            # Save encrypted password and key
            with open('saved_passwords.json', 'w') as f:
                json.dump({"key": key.decode(), "password": cipher_text.decode()}, f)

            messagebox.showinfo("Success", "Password has been saved successfully!")

    def copy_password(self):
        self.root.clipboard_clear()  # clear clipboard contents
        self.root.clipboard_append(self.password_entry.get())  # append new value to clipbaord


root = tk.Tk()
root.minsize(150, 150)  # minimum size the window can be resized to
root.maxsize(450, 250)  # maximum size the window can be resized to
app = PasswordGenerator(root)
root.mainloop()
