import tkinter as tk
from tkinter import messagebox

def add_task():
    """Add a task to the list."""
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    tasks_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def delete_task():
    """Delete the selected task."""
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    """Clear all tasks."""
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks_listbox.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Frame for the task input and buttons
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Entry for new tasks
task_entry = tk.Entry(input_frame, width=25, font=("Arial", 14))
task_entry.pack(side=tk.LEFT, padx=10)

# Button to add a task
add_button = tk.Button(input_frame, text="Add Task", command=add_task, bg="lightgreen", font=("Arial", 12))
add_button.pack(side=tk.LEFT)

# Listbox for displaying tasks
tasks_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12), selectmode=tk.SINGLE)
tasks_listbox.pack(pady=10)

# Frame for action buttons
action_frame = tk.Frame(root)
action_frame.pack(pady=10)

# Button to delete a selected task
delete_button = tk.Button(action_frame, text="Delete Task", command=delete_task, bg="lightblue", font=("Arial", 12))
delete_button.pack(side=tk.LEFT, padx=10)

# Button to clear all tasks
clear_button = tk.Button(action_frame, text="Clear All", command=clear_tasks, bg="lightcoral", font=("Arial", 12))
clear_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()
