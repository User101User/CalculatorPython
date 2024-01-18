from tkinter import *
from ttkthemes import ThemedTk
from tkinter import ttk




window = ThemedTk (theme = "equilux")
window.configure(themebg = "equilux")

window.geometry("460x185")

window.title("Calculator")

var = StringVar()
result = ""


def clear():
   global result
   result = ""
   var.set("")

def press(num):
    global result
    result = result + str(num)
    var.set(result)

def equalpress():
    try:
        global result
        total = str(eval(result))
        var.set(total)
        result = ""

    except:
        var.set("------ERROR------")
        result = ""





def backspace():
    global result
    result = txt.get()[:-1]
    if result == "":
        result = ""
    var.set(result)

txt = ttk.Entry(window,width=32, font=("Arial", 20), text=var)
txt.grid(column=0, row=0, columnspan=4)

btn1 = ttk.Button(window, width=10 ,text="1",command=lambda: press(1))
btn1.grid(column=0, row=1)
btn2 = ttk.Button(window, width=10 ,text="2",command=lambda: press(2))
btn2.grid(column=1, row=1)
btn3 = ttk.Button(window, width=10 ,text="3",command=lambda: press(3))
btn3.grid(column=2, row=1)
btn4 = ttk.Button(window, width=10 ,text="4",command=lambda: press(4))
btn4.grid(column=3, row=1)
btn5 = ttk.Button(window, width=10 ,text="5",command=lambda: press(5))
btn5.grid(column=0, row=2)
btn6 = ttk.Button(window, width=10 ,text="6",command=lambda: press(6))
btn6.grid(column=1, row=2)
btn7 = ttk.Button(window, width=10 ,text="7",command=lambda: press(7))
btn7.grid(column=2, row=2)
btn8 = ttk.Button(window, width=10 ,text="8",command=lambda: press(8))
btn8.grid(column=3, row=2)
btn9 = ttk.Button(window, width=10 ,text="9", command=lambda: press(9))
btn9.grid(column=0, row=3)
btn0 = ttk.Button(window, width=10 ,text="0",command=lambda: press(0))
btn0.grid(column=0, row=4)
btn10 = ttk.Button(window, width=10 ,text="-",command=lambda: press("-"))
btn10.grid(column=1, row=3)
btn11 = ttk.Button(window, width=10 ,text="+", command=lambda: press("+"))
btn11.grid(column=2, row=3)
btn12 = ttk.Button(window, width=10 ,text="*",command=lambda: press("*"))
btn12.grid(column=3, row=3)
btn13 = ttk.Button(window, width=10 ,text= "/",command=lambda:press("/"))
btn13.grid(column=1, row=4)
btn14 = ttk.Button(window, width=10 ,text="AC", command=clear)
btn14.grid(column=2, row=4)
btn15 = ttk.Button(window, width=10 ,text="DEL",command=backspace)
btn15.grid(column=3, row=4)
btn16 = ttk.Button(window, width=10 ,text="=",command=equalpress)
btn16.grid(column=1, row=5)
btn17 = ttk.Button(window, width=10 ,text=".",command=lambda: press("."))
btn17.grid(column=0, row=5)
btn18 = ttk.Button(window, width=10 ,text="(",command=lambda: press("("))
btn18.grid(column=2, row=5)
btn19 = ttk.Button(window, width=10 ,text=")",command=lambda: press(")"))
btn19.grid(column=3, row=5)

window.mainloop()