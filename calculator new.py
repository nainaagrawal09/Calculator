from tkinter import *
import math
from sympy import symbols,solve

root=Tk()
root.title("Calculator")
root.geometry("600x400")
root.configure(background="black")

def click(event):
    global var
    t=event.widget.cget("text")
    if t=="=":
        if var.get().isdigit():
            val=int(var.get())
        else:
            try:
                val=eval(var.get())
            except Exception as e:
                val="Error"
                print(e)
        var.set(val)
        screen.update()
    elif t=="C":
        var.set("")
        screen.update()
    elif t=="Bksp":
        var.set(var.get()[:-1])
        screen.update()
    elif t=="mod":
        var.set(var.get()+"%")
        screen.update()
    elif t=="sq":
        var.set(var.get()[:-1]+"("+var.get()[-1]+"**2)")
        screen.update()
    elif t=="pow":
        var.set(var.get()+"**")
        screen.update()
    elif t=="log2":
        if var.get().isdigit():
            val=int(var.get())
        else:
            try:
                val=eval(var.get())
            except Exception as e:
                val="Error"
                print(e)
        try:
            result = str(math.log2(val))
        except:
            result="error"
        var.set(result)
        screen.update()
    elif t=="log10":
        if var.get().isdigit():
            val=int(var.get())
        else:
            try:
                val=eval(var.get())
            except Exception as e:
                val="Error"
                print(e)
        try:
            result = str(math.log10(val))
        except:
            result="error"
        var.set(result)
        screen.update()
    elif t=="ln":
        if var.get().isdigit():
            val=int(var.get())
        else:
            try:
                val=eval(var.get())
            except Exception as e:
                val="Error"
                print(e)
        try:
            result = str(math.log(val))
        except:
            result="error"
        var.set(result)
        screen.update()
    elif t=="sin":
        if var.get().isdigit():
            val=int(var.get())
        else:
            try:
                val=eval(var.get())
            except Exception as e:
                val="Error"
                print(e)
        result = str(math.sin(math.radians(int(val))))
        var.set(result)
        screen.update()
    elif t=="cos":
        if var.get().isdigit():
            val=int(var.get())
        else:
            try:
                val=eval(var.get())
            except Exception as e:
                val="Error"
                print(e)
        result = str(math.cos(math.radians(int(val))))
        var.set(result)
        screen.update()
    elif t=="tan":
        if var.get().isdigit():
            val=int(var.get())
        else:
            try:
                val=eval(var.get())
            except Exception as e:
                val="Error"
                print(e)
        result = str(math.tan(math.radians(int(val))))
        var.set(result)
        screen.update()
    elif t=="sinh":
        if var.get().isdigit():
            val=int(var.get())
        else:
            try:
                val=eval(var.get())
            except Exception as e:
                val="Error"
                print(e)
        result = str(math.sinh(math.radians(int(val))))
        var.set(result)
        screen.update()
    elif t=="sqrt":
        if var.get().isdigit():
            val=int(var.get())
        else:
            try:
                val=eval(var.get())
            except Exception as e:
                val="Error"
                print(e)
        result = math.sqrt(float(val))
        var.set(result)
        screen.update()
    else:
        var.set(var.get()+t)
        screen.update()

def expr():
    global var
    x = symbols('x')
    temp=var.get()
    sol = solve(eval(temp))
    var.set(sol)
    screen.update()

def getx():
    global var
    var.set(var.get() + "x")
    screen.update()


cal_operator=""
var=StringVar()
var.set("")
screen=Entry(root,textvar=var,font="lucida 23 bold",relief=SUNKEN)
screen.pack(fill="both",padx=8,pady=6)

l=["00","0",".","=","sq","pow","(",")","1","2","3","+",
   "log2","log10","ln","sinh","4","5","6","-","sin","cos","tan","sqrt","7","8","9","*","C","mod","Bksp","/"]


k=0
for i in range(0,4):
    f = Frame(root, bg="orange")
    for j in range (0,8):
        b = Button(f, text=l[k], font="lucida 9 bold", width=9, height=3)
        b.pack(side=LEFT, padx=1,pady=1)
        b.bind("<Button-1>",click)
        k=k+1
    f.pack(side=BOTTOM, anchor="w")

ff=Frame(root,bg="orange")
b = Button(ff, text="expr", font="lucida 9 bold", width=9, height=2,command=expr)
b2 = Button(ff, text="x", font="lucida 9 bold", width=9, height=2,command=getx)
b.pack(side=LEFT, padx=1,pady=1)
b2.pack(side=LEFT,padx=1,pady=1)
ff.pack(side=BOTTOM, anchor="e")

root.maxsize(600,400)
root.minsize(600,400)
root.mainloop()
