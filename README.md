# To-Do-List-Application-tkinter-

Features:
Add Task: Users can type a task into the entry box and click the "Add Task" button to add it to the list.

Delete Task: Select a task in the list and click the "Delete Task" button to remove it.

Clear All: Deletes all tasks after confirmation.

Interactive UI: Uses a tk.Listbox widget to display tasks and tk.Entry for input.

How It Works: Adding Tasks: The task_entry widget is used to input text. The tasks_listbox.insert() method appends the task to the listbox.

Deleting a Task: The tasks_listbox.curselection() method gets the selected task's index. The tasks_listbox.delete() method removes the task at the selected index.

Clearing All Tasks: The tasks_listbox.delete(0, tk.END) method clears all items in the listbox.

Warning and Confirmation: messagebox.showwarning() is used to warn users if no task is selected or if the task entry is empty. messagebox.askyesno() prompts the user for confirmation before clearing all tasks.

![Screenshot 2024-11-25 143538](https://github.com/user-attachments/assets/3786a530-aa9f-43e3-916a-f31c484d5092)
