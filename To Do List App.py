import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.listbox = tk.Listbox(
            self.frame, 
            width=50, 
            height=10, 
            selectmode=tk.SINGLE
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        self.entry = tk.Entry(
            self.root, 
            font=('calibri', 12)
        )
        self.entry.pack(pady=20)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)
        
        self.add_button = tk.Button(
            self.button_frame, 
            text="Add Task", 
            command=self.add_task
        )
        self.add_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_button = tk.Button(
            self.button_frame, 
            text="Delete Task", 
            command=self.delete_task
        )
        self.delete_button.pack(side=tk.LEFT, padx=10)
        
        self.update_button = tk.Button(
            self.button_frame, 
            text="Update Task", 
            command=self.update_task
        )
        self.update_button.pack(side=tk.LEFT, padx=10)
    
    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self):
        task_index = self.listbox.curselection()
        if task_index:
            task = self.listbox.get(task_index)
            self.tasks.remove(task)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def update_task(self):
        task_index = self.listbox.curselection()
        if task_index:
            new_task = self.entry.get()
            if new_task:
                self.tasks[task_index[0]] = new_task
                self.update_listbox()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        else:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "_main_":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()