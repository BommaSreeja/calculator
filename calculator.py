from tkinter import*
exp=""
def press(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)
def equal_press():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        exp=""
    except:
        equation.set("error")
        exp=""
def cl():
    global exp
    exp=""
    equation.set("")
def delete():
    global exp
    exp=exp[:-1]
    equation.set(exp)

root=Tk()
root.title("Calculator")
root.geometry("400x400")
equation=StringVar()
txt=Entry(root,textvariable=equation)
txt.grid(columnspan=4,row=1,ipadx=30)
button1=Button(root,text='1',fg='black',command=lambda: press(1),height=3,width=7)
button1.grid(row=5,column=0)
button2=Button(root,text='2',fg='black',command=lambda: press(2),height=3,width=7)
button2.grid(row=5,column=1)
button3=Button(root,text='3',fg='black',command=lambda: press(3),height=3,width=7)
button3.grid(row=5,column=2)
button4=Button(root,text='4',fg='black',command=lambda: press(4),height=3,width=7)
button4.grid(row=4,column=0)
button5=Button(root,text='5',fg='black',command=lambda: press(5),height=3,width=7)
button5.grid(row=4,column=1)
button6=Button(root,text='6',fg='black',command=lambda: press(6),height=3,width=7)
button6.grid(row=4,column=2)
button7=Button(root,text='7',fg='black',command=lambda: press(7),height=3,width=7)
button7.grid(row=3,column=0)
button8=Button(root,text='8',fg='black',command=lambda: press(8),height=3,width=7)
button8.grid(row=3,column=1)
button9=Button(root,text='9',fg='black',command=lambda: press(9),height=3,width=7)
button9.grid(row=3,column=2)
button0=Button(root,text='0',fg='black',command=lambda: press(0),height=3,width=7)
button0.grid(row=6,column=1)
Add=Button(root,text='+',fg='black',command=lambda: press('+'),height=3,width=7)
Add.grid(row=5,column=3)
minus=Button(root,text='-',fg='black',command=lambda: press('-'),height=3,width=7)
minus.grid(row=4,column=3)
multiply=Button(root,text='*',fg='black',command=lambda: press('*'),height=3,width=7)
multiply.grid(row=3,column=3)
divide=Button(root,text='/',fg='black',command=lambda: press('/'),height=3,width=7)
divide.grid(row=2,column=3)
remainder=Button(root,text='%',fg='black',command=lambda:press('%'),height=3,width=7)
remainder.grid(row=2,column=2)
power=Button(root,text='^',fg='black',command=lambda:press(''),height=3,width=7)
power.grid(row=6,column=0)
equal=Button(root,text='=',fg='black',command=equal_press,height=3,width=7)
equal.grid(row=6,column=3)
clear=Button(root,text='Clear',fg='black',command=cl,height=3,width=7)
clear.grid(row=2,column=0)
remove=Button(root,text='DEL',fg='black',command=delete,height=3,width=7)
remove.grid(row=2,column=1)
Decimal=Button(root,text='.',fg='black',command=lambda: press('.'),height=3,width=7)
Decimal.grid(row=6,column=2)
root.mainloop()