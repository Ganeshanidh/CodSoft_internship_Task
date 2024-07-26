import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), 
                      command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid operation: {e}")
        else:
            current_text = self.entry.get()
            new_text = current_text + str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, new_text)

if __name__ == "_main_":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()