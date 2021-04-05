from tkinter import *

window=Tk()
window.geometry("350x460")
window.title="calculator"
headlabel=Label(window,text="CALCULATOR",bg='dark gray',font=('times',16)).pack(side=TOP)
window.config(background="light blue")

input=StringVar()
operator=""

def clickbutton(number):
    global operator
    operator=operator+str(number)
    input.set(operator)

def operatorbutton():
    global operator
    add=str(eval(operator))
    input.set(add)
    operator=add

def clear():
    global  operator
    input.set('')
    operator=''

inputtext=Entry(window,font=("courier new",12,'bold'),textvar=input,width=25,bd=5,bg='powder blue').pack()
button1=Button(window,command=lambda:clickbutton(1),text='1',padx=14,pady=14,font=('courier new',12,'bold')).place(x=10,y=100)
button2=Button(window,command=lambda:clickbutton(2),text='2',padx=14,pady=14,font=('courier new',12,'bold')).place(x=75,y=100)
button3=Button(window,command=lambda:clickbutton(3),text='3',padx=14,pady=14,font=('courier new',12,'bold')).place(x=140,y=100)
button4=Button(window,command=lambda:clickbutton(4),text='4',padx=14,pady=14,font=('courier new',12,'bold')).place(x=10,y=170)
button5=Button(window,command=lambda:clickbutton(5),text='5',padx=14,pady=14,font=('courier new',12,'bold')).place(x=75,y=170)
button6=Button(window,command=lambda:clickbutton(6),text='6',padx=14,pady=14,font=('courier new',12,'bold')).place(x=140,y=170)
button7=Button(window,command=lambda:clickbutton(7),text='7',padx=14,pady=14,font=('courier new',12,'bold')).place(x=10,y=240)
button8=Button(window,command=lambda:clickbutton(8),text='8',padx=14,pady=14,font=('courier new',12,'bold')).place(x=75,y=240)
button9=Button(window,command=lambda:clickbutton(9),text='9',padx=14,pady=14,font=('courier new',12,'bold')).place(x=140,y=240)
button0=Button(window,command=lambda:clickbutton(0),text='0',padx=14,pady=14,font=('courier new',12,'bold')).place(x=75,y=310)
buttondot=Button(window,command=lambda:clickbutton('.'),text='.',padx=14,pady=14,font=('courier new',12,'bold')).place(x=10,y=310)
buttonadd=Button(window,command=lambda:clickbutton('+'),text='+',padx=14,pady=14,font=('courier new',12,'bold')).place(x=205,y=100)
buttonsub=Button(window,command=lambda:clickbutton('-'),text='-',padx=14,pady=14,font=('courier new',12,'bold')).place(x=205,y=170)
buttondiv=Button(window,command=lambda:clickbutton('/'),text='/',padx=14,pady=14,font=('courier new',12,'bold')).place(x=205,y=240)
buttonmul=Button(window,command=lambda:clickbutton('*'),text='*',padx=14,pady=14,font=('courier new',12,'bold')).place(x=205,y=310)
buttonequal=Button(window,command=operatorbutton,text='=',padx=14,pady=14,font=('courier new',12,'bold')).place(x=140,y=310)
buttonclear=Button(window,command=clear,text='CE',padx=14,pady=14,font=('courier new',12,'bold')).place(x=270,y=170)
buttonpower=Button(window,command=exit,text='AC',padx=14,pady=14,font=('courier new',12,'bold')).place(x=270,y=100)
buttonexp=Button(window,command=lambda:clickbutton('**'),text='**',padx=14,pady=14,font=('courier new',12,'bold')).place(x=10,y=380)
buttonbracketstart=Button(window,command=lambda:clickbutton('('),text='(',padx=14,pady=14,font=('courier new',12,'bold')).place(x=270,y=310)
buttonbracketend=Button(window,command=lambda:clickbutton(')'),text=')',padx=14,pady=14,font=('courier new',12,'bold')).place(x=270,y=240)
window.mainloop()