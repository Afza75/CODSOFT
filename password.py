from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

m = Tk()
m.title("password generator")
select=tk.StringVar()
def generator():
    length =int(enter_difficulty.get())
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    letter = string.digits
    special = string.punctuation
    all_chars = lowercase + uppercase + letter

    difficulty= select.get()

    if length<=0 :
        messagebox.showerror("error","invalid length")

    elif difficulty=="Normal":
        password_list = random.sample(lowercase+uppercase+letter, length)
        password = ""
        for i in password_list:
            password = password + i
        display_password.config(text=f"{password}")

    elif difficulty=="Easy":
        password_list = random.sample(lowercase+letter, length)
        password = ""
        for i in password_list:
            password = password + i
        display_password.config(text=f"{password}")

    elif difficulty=="Difficult":
        password_list = random.sample(lowercase+letter+uppercase+special, length)
        password = ""
        for i in password_list:
            password = password + i
        display_password.config(text=f"{password}")


main = Label(m, text="PASSWORD GENERATOR", bg="#76ABAE", font=16)
main.grid(row=0, column=0, padx=10, pady=10)

length_password = Label(m, text="Enter Length of Password:", bg="#31363F", fg="white", font=14)
length_password.grid(row=1, column=0, padx=10, pady=10)

enter_difficulty = Entry(m, bg="white", fg="#31363F", width=25,font=8)
enter_difficulty.grid(row=2, column=0, padx=10, pady=10)

difficulty_password= Label(m, text="Choose Difficulty Level:", bg="#31363F", fg="white", font=15,width=20)
difficulty_password.grid(row=3, column=0, padx=10, pady=10)

combo_box = ttk.Combobox(m, values=["Easy", "Normal", "Difficult"], textvariable=select,width=24,font=8)
combo_box.set("Easy")
combo_box.grid(row=4, column=0, padx=10, pady=10)

password = Label(m, text="Password:", bg="#31363F", fg="white", font=15,width=20)
password.grid(row=5, column=0, padx=10, pady=10)

display_password = Label(m, bg="white", fg="#31363F", width=25,font=8)
display_password.grid(row=6, column=0, padx=10, pady=10)

generate_button= Button(m, text="GENERATE PASSWORD", bg="#76ABAE",width=24, command=generator)
generate_button.grid(row=7, column=0, padx=10, pady=10)

m.mainloop()
