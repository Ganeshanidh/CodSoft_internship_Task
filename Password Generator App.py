import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGeneratorApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label = tk.Label(root, text="Password Length:", font=('Arial', 14))
        self.label.pack(pady=10)

        self.length_var = tk.IntVar()
        self.length_entry = tk.Entry(root, textvariable=self.length_var, font=('Arial', 14))
        self.length_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=('Arial', 14))
        self.generate_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=('Arial', 14))
        self.result_label.pack(pady=10)

    def generate_password(self):
        length = self.length_var.get()
        if length <= 0:
            messagebox.showwarning("Warning", "Please enter a valid password length.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        
        self.result_label.config(text=f"Generated Password: {password}")

if __name__ == "_main_":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()