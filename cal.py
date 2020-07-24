from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("400x550")
root.wm_iconbitmap("1.ico")
root.title("Calculator")
def click(event):
    global var
    # print("hey")
    # event.widget gives the button that has been clicked
    # cget() is used to extraxt text of a widget(like button)
    # print(event.widget.cget("text"))
    if event.widget.cget("text") == "=":
        if var.get().isdigit():
            val = int(var.get())
        else:
            try:
                val = eval(sc.get())
            except Exception as e:
                print((e))
                val = "Error"
        var.set(val)
        sc.update()
    elif event.widget.cget("text") == "C":
        var.set("")
        sc.update()
    else:
        var.set(var.get()+event.widget.cget("text"))
        # update func forces the widget to update it's value
        sc.update()

var = StringVar()
var.set("")
sc = Entry(root, textvar=var, font="lucida 28")
sc.pack(fill="x", padx=10, pady=8)

f = Frame(root, bg="grey")
b = Button(f, text="7", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
b = Button(f, text="8", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
b = Button(f, text="9", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="4", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
b = Button(f, text="5", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
b = Button(f, text="6", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="1", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
b = Button(f, text="2", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
b = Button(f, text="3", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="0", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
b = Button(f, text="=", font="lucida 25 bold", padx=18, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
b = Button(f, text="C", font="lucida 25 bold", padx=15, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="-", font="lucida 25 bold", padx=20, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
b = Button(f, text="+", font="lucida 25 bold", padx=19, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
b = Button(f, text="*", font="lucida 25 bold", padx=20, pady=8)
b.pack(side="left", padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()
