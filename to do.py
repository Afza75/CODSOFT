from tkinter import *
from tkinter import messagebox

completed_tasks = []
deadline_tasks = []

def add_task():
    task = entry.get()
    listbox_tasks.insert(END, task)
    entry.delete(0, "end")

def delete_task():
    selected_index = listbox_tasks.curselection()
    if selected_index:
        task = listbox_tasks.get(selected_index)
        listbox_tasks.delete(selected_index)
        if task in completed_tasks:
            completed_tasks.remove(task)
        if task in deadline_tasks:
            deadline_tasks.remove(task)

def update_task():
    selected_index = listbox_tasks.curselection()
    if selected_index:
        listbox_tasks.delete(selected_index)
        task = entry.get()
        entry.delete(0, "end")
        listbox_tasks.insert(selected_index, task)

def track_task():
    selected_index = listbox_tasks.curselection()
    if selected_index:
        task = listbox_tasks.get(selected_index)
        track_menu = Menu(root, tearoff=0)
        track_menu.add_command(label="Completed", command=lambda: tracking_option("Completed", task))
        track_menu.add_command(label="Approaching Deadline", command=lambda: tracking_option("Approaching Deadline", task))
        track_menu.post(button_track.winfo_rootx(), button_track.winfo_rooty() + button_track.winfo_height())

def tracking_option(option, task):
    if option == "Completed":
        if task not in completed_tasks:
            completed_tasks.append(task)
            listbox_tasks.itemconfig(listbox_tasks.curselection(), {'bg': '#41C9E2'})  # Highlight completed task
    elif option == "Deadline is near":
        if task not in deadline_tasks:
            deadline_tasks.append(task)
            listbox_tasks.itemconfig(listbox_tasks.curselection(), {'bg': '#FA7070'})  # Highlight deadline task

def display_task_completed_or_not():
    total_tasks = listbox_tasks.size()
    completed_count = len(completed_tasks)
    remaining_count = total_tasks - completed_count
    message = f"Total tasks: {total_tasks}\nCompleted tasks: {completed_count}\nRemaining tasks: {remaining_count}\n\n"
    if deadline_tasks:
        message += "Deadline Tasks:\n"
        for task in deadline_tasks:
            message = message + f"- {task}\n"
    messagebox.showinfo("Task Stats", message)

root = Tk()
root.title('To-Do List')
root.config(bg='#f0f0f0')

listbox_tasks = Listbox(root, width=40, height=8, font=('Arial', 14), fg='#333333')
listbox_tasks.grid(row=0, column=0, padx=10, pady=10)

entry = Entry(root, font=('Arial', 18))
entry.grid(row=1, column=0, padx=10, pady=10)

button_add = Button(root, text='Add Task', font=('Arial', 12), bg='#8CB9BD', padx=20, pady=10, command=add_task)
button_add.grid(row=2, column=0, padx=10, pady=10)

button_update = Button(root, text='Update Task', font=('Arial', 12), bg='#C68484', padx=20, pady=10, command=update_task)
button_update.grid(row=3, column=0, padx=10, pady=10)

button_delete = Button(root, text='Delete Task', font=('Arial', 12), bg='#A3C9AA', padx=20, pady=10, command=delete_task)
button_delete.grid(row=4, column=0, padx=10, pady=10)

button_track = Button(root, text='Track Progress', font=('Arial', 12), bg='#E6D5B8', padx=20, pady=10, command=track_task)
button_track.grid(row=5, column=0, padx=10, pady=10)

button_stats = Button(root, text='Task Overview', font=('Arial', 12), bg='#B3C8CF', padx=20, pady=10, command=display_task_completed_or_not)
button_stats.grid(row=6, column=0, padx=10, pady=10)

root.mainloop()




# from tkinter import *
#
# def add_task():
#     task = entry.get()
#     listbox_tasks.insert(END,task)
#     entry.delete(0, "end")
#
#
# def delete_task():
#         listbox_tasks.delete(listbox_tasks.curselection())
#
#
# def update_task():
#         listbox_tasks.delete(listbox_tasks.curselection())
#         task = entry.get()
#         entry.delete(0, "end")
#         listbox_tasks.insert(END, task)
#
#
# root = Tk()
# root.title('To-Do List')
# root.config(bg='#f0f0f0')
#
#
#
#
# listbox_tasks = Listbox(root,width=40,height=8,font=('Arial', 14),fg='#333333')
# listbox_tasks.grid(row=0,column=0,padx=10,pady=10)
#
# entry = Entry(root,font=('Arial', 18))
# entry.grid(row=1,column=0,padx=10,pady=10)
#
# button_add = Button(root,text='Add Task',font=('Arial', 12),bg='#8CB9BD',padx=20,pady=10, command=add_task)
# button_add.grid(row=2,column=0,padx=10,pady=10)
#
# button_update = Button(root,text='Update Task',font=('Arial', 12),bg='#C68484',padx=20,pady=10,command=update_task)
# button_update.grid(row=3,column=0,padx=10,pady=10)
#
# button_delete = Button(root,text='Delete Task',font=('Arial', 12),bg='#A3C9AA',padx=20,pady=10,command=delete_task)
# button_delete.grid(row=4,column=0,padx=10,pady=10)
#
# root.mainloop()






