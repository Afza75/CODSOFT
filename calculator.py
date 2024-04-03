from tkinter import *

root=Tk()
root.title("scientific calculator")
e=Entry(root,width=50,relief=RIDGE,borderwidth=2,fg="white",bg="black")
e.grid(row=0,column=0,padx=10,pady=15,columnspan=4)
#root.configure(bg='black')

def click(to_print):
    old=e.get()
    e.delete(0, END)
    e.insert(0,old+to_print)

def clear():
    e.delete(0,END)
    return

def bkps():
    current=e.get()
    length=len(current)-1
    e.delete(length, END)

def evaluate(): #take string
    ans=e.get()
    ans=eval(ans)
    e.delete(0,END)
    e.insert(0, ans)

Button(root, text="0", bg="grey", width=6, height=2, command=lambda: click("0")).grid(row=1, column=3)
Button(root, text="1", width=6, height=2, command=lambda: click("1")).grid(row=6, column=0)
Button(root, text="2", width=6, height=2, command=lambda: click("2")).grid(row=6, column=1)
Button(root, text="3", width=6, height=2, command=lambda: click("3")).grid(row=6, column=2)
Button(root, text="4", width=6, height=2, command=lambda: click("4")).grid(row=5, column=0)
Button(root, text="5", width=6, height=2, command=lambda: click("5")).grid(row=5, column=1)
Button(root, text="6", width=6, height=2, command=lambda: click("6")).grid(row=5, column=2)
Button(root, text="7", width=6, height=2, command=lambda: click("7")).grid(row=4, column=0)
Button(root, text="8", width=6, height=2, command=lambda: click("8")).grid(row=4, column=1)
Button(root, text="9", width=6, height=2, command=lambda: click("9")).grid(row=4, column=2)

Button(root, text="/",bg="grey",  width=6, height=2, command=lambda: click("/")).grid(row=4, column=3)
Button(root, text="+",bg="grey",  width=6, height=2, command=lambda: click("+")).grid(row=7, column=3)
Button(root, text="*",bg="grey",  width=6, height=2, command=lambda: click("*")).grid(row=5, column=3)
Button(root, text="-",bg="grey",  width=6, height=2, command=lambda: click("-")).grid(row=6, column=3)

Button(root, text=".",bg="grey", width=6, height=2, command=lambda: click(".")).grid(row=1, column=2)
Button(root, text="(",bg="grey",  width=6, height=2, command=lambda: click("(")).grid(row=1, column=0)
Button(root, text=")",bg="grey",  width=6, height=2, command=lambda: click(")")).grid(row=1, column=1)

Button(root, text="AC",bg="yellow", width=6, height=2, command=clear).grid(row=7, column=0)
Button(root, text="←",bg="yellow", width=6, height=2, command=bkps).grid(row=7, column=1)
Button(root, text="=", bg="yellow", width=6, height=2, command=evaluate).grid(row=7, column=2)

root.mainloop()
