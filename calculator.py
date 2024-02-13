import tkinter
from tkinter import*
from tkinter import messagebox

val =""
A=0
operator = ""

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_clicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_clicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_clicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_clicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_clicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_clicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_clicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_clicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_clicked():
    global val
    val = val + "0"
    data.set(val)

def btn_plus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_min_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mult_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def c_pressed():
    global A
    global operator
    global val
    val =""
    A=0
    operator =  ""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2=val

    if operator == "+":
        x=int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val =  str(c)
    elif operator == "-":
        x=int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val =  str(c)
    elif operator == "*":
        x=int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val =  str(c)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error","Division By 0 Not Supported")
            A = ""
            val =  ""
            data.set(val)
        else:
            c = int(A/x) 
            data.set(c)  
            val = str(c) 
    

root=tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("calculator")

data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("verdana", 20),
    textvariable= data,
    background= "#ffffff",
    fg="#000000",
)
lbl.pack(expand= True, fill = "both",)

btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand = True,fill = "both", )

btnrow2 = Frame(root)
btnrow2.pack(expand = True,fill = "both", )

btnrow3 = Frame(root)
btnrow3.pack(expand = True,fill = "both", )

btnrow4 = Frame(root)
btnrow4.pack(expand = True,fill = "both", )

btn1 = Button(
    btnrow1,
    text = "1",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_2_clicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_3_clicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_plus_clicked,
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)



btn1 = Button(
    btnrow2,
    text = "4",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_4_clicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow2,
    text = "5",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_5_clicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow2,
    text = "6",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_6_clicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_min_clicked
)
btnminus.pack(side = LEFT, expand = True, fill = "both",)


btn1 = Button(
    btnrow3,
    text = "7",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_7_clicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow3,
    text = "8",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_8_clicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow3,
    text = "9",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_9_clicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_mult_clicked,
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)


btnc = Button(
    btnrow4,
    text = "C",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=c_pressed,
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow4,
    text = "0",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_0_clicked

)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command= result,

)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("verdana",22),
    relief=GROOVE,
    border = 0,
    command=btn_div_clicked,
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)


root.mainloop()