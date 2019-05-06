from tkinter import *

def bt(numbers):
    global operator
    operator=operator+str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    operator=''
    txt_input.set(operator)
    #Display.insert(0,'start calculating')

def equal():
    global operator
    sumup=float(eval(operator))
    txt_input.set(sumup)
    operator=''



root =Tk()
root.title('calculator')

operator=''
txt_input=StringVar(value="start calculating...")



display=Entry(root,font=('arial',30,'bold'),fg='white',bg='grey',justify='right',bd=50,textvariable=txt_input)
display.grid(columnspan=4)

bt7=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='7',command=lambda:bt(7)).grid(row=1,column=0)
bt8=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='8',command=lambda:bt(8)).grid(row=1,column=1)
bt9=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='9',command=lambda:bt(9)).grid(row=1,column=2)
btc=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='c',bg='green',command=clear).grid(row=1,column=3)

bt4=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='4',command=lambda:bt(4)).grid(row=2,column=0)
bt5=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='5',command=lambda:bt(5)).grid(row=2,column=1)
bt6=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='6',command=lambda:bt(6)).grid(row=2,column=2)
btplus=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='+',command=lambda:bt('+')).grid(row=2,column=3)

bt1=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='1',command=lambda:bt(1)).grid(row=3,column=0)
bt2=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='2',command=lambda:bt(2)).grid(row=3,column=1)
bt3=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='3',command=lambda:bt(3)).grid(row=3,column=2)
btminus=Button(root,padx=35,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='-',command=lambda:bt('-')).grid(row=3,column=3)

bt0=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='0',command=lambda:bt(0)).grid(row=4,column=0)
btdot=Button(root,padx=35,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='.',command=lambda:bt('.')).grid(row=4,column=1)
btdivison=Button(root,padx=35,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='/',command=lambda:bt('/')).grid(row=4,column=2)
btmultiply=Button(root,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='x',command=lambda:bt('*')).grid(row=4,column=3)

btequal=Button(root,padx=95,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='=',bg='red',command=equal).grid(row=5,column=0,columnspan=2)
btopenbrack=Button(root,padx=35,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='(',command=lambda:bt('(')).grid(row=5,column=2)
btclosebrack=Button(root,padx=35,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=')',command=lambda:bt(')')).grid(row=5,column=3)


root.mainloop()