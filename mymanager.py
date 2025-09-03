import tkinter as tk
from tkinter import simpledialog, messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Task Manager")
        self.root.geometry("400x500")

        # Task list
        self.tasks = []

        # Input frame
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.task_entry = tk.Entry(frame, width=25, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT, padx=5)

        add_button = tk.Button(frame, text="➕ Add", command=self.add_task)
        add_button.pack(side=tk.LEFT)

        # Task listbox
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        edit_button = tk.Button(button_frame, text="✏️ Edit", command=self.edit_task)
        edit_button.grid(row=0, column=0, padx=5)

        complete_button = tk.Button(button_frame, text="✅ Complete", command=self.complete_task)
        complete_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(button_frame, text="❌ Delete", command=self.delete_task)
        delete_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"title": task, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def edit_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            old_task = self.tasks[index]["title"]
            new_task = simpledialog.askstring("Edit Task", "Update task:", initialvalue=old_task)
            if new_task:
                self.tasks[index]["title"] = new_task
                self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to edit!")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete!")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task["completed"]:
                self.task_listbox.insert(tk.END, f"✅ {task['title']}")
            else:
                self.task_listbox.insert(tk.END, f"📌 {task['title']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
