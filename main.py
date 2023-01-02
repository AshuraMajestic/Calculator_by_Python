from tkinter import *
from turtle import right
k=Tk()
k.geometry("350x500")
k.resizable(0,0)

def disp(number):
    global num
    num=num+str(number)
    label1['text']=num

def clear():
    global num
    num=""
    label1['text']=num
def evalute():
    global num
    result=str(eval(num))
    label1['text']=result
    num=result

num=''
frame1=Frame(k)
frame1.pack(expand=TRUE,fill=BOTH)
frame2=Frame(k)
frame2.pack(expand=TRUE,fill=BOTH)
frame3=Frame(k)
frame3.pack(expand=TRUE,fill=BOTH)
frame4=Frame(k)
frame4.pack(expand=TRUE,fill=BOTH)
label1=Label(frame1,textvariable="",font=("cascadia code",20),anchor=SE,bg="#190207",fg="white")
label1.pack(expand=TRUE,fill=BOTH)

key1=Button(frame1,text="1",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp(1))
key1.pack(expand=TRUE,fill=BOTH,side=LEFT)
key2=Button(frame1,text="2",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp(2))
key2.pack(expand=TRUE,fill=BOTH,side=LEFT)
key3=Button(frame1,text="3",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp(3))
key3.pack(expand=TRUE,fill=BOTH,side=LEFT)
key_addition=Button(frame1,text="+",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp("+"))
key_addition.pack(expand=TRUE,fill=BOTH,side=LEFT)

key4=Button(frame2,text="4",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp(4))
key4.pack(expand=TRUE,fill=BOTH,side=LEFT)
key5=Button(frame2,text="5",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp(5))
key5.pack(expand=TRUE,fill=BOTH,side=LEFT)
key6=Button(frame2,text="6",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp(6))
key6.pack(expand=TRUE,fill=BOTH,side=LEFT)
key_substraction=Button(frame2,text="-",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp("-"))
key_substraction.pack(expand=TRUE,fill=BOTH,side=LEFT)

key7=Button(frame3,text="7",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp(7))
key7.pack(expand=TRUE,fill=BOTH,side=LEFT)
key8=Button(frame3,text="8",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp(8))
key8.pack(expand=TRUE,fill=BOTH,side=LEFT)
key9=Button(frame3,text="9",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp(9))
key9.pack(expand=TRUE,fill=BOTH,side=LEFT)
key_multiplication=Button(frame3,text="*",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp("*"))
key_multiplication.pack(expand=TRUE,fill=BOTH,side=LEFT)

key_clear=Button(frame4,text="C",font=("cascadia code",20),border=4,bg="#9D0B28",fg="gold",command=clear)
key_clear.pack(expand=TRUE,fill=BOTH,side=LEFT)
key_0=Button(frame4,text="0",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp(0))
key_0.pack(expand=TRUE,fill=BOTH,side=LEFT)
key_equalto=Button(frame4,text="=",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=evalute)
key_equalto.pack(expand=TRUE,fill=BOTH,side=LEFT)
key_divison=Button(frame4,text="/",font=("cascadia code",20),border=4,bg="#9D0B28",fg="white",command=lambda:disp("/"))
key_divison.pack(expand=TRUE,fill=BOTH,side=LEFT)

k.mainloop()
