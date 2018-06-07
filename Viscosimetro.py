from tkinter import *
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.commondialog import Dialog
from tkinter.filedialog import *
import serial
import matplotlib.pyplot as plt
import numpy as np

e = serial.Serial("COM5", 9600)
print("Conectado")
root= Tk();

def salir():
    e.close()
    root.destroy()
    flog=open('log.txt','a')
    flog.write('\nEnd\n')
    flog.close()
    
root.configure(bg="white")
flog=open('log.txt','a')
flog.write('\nBegin')
flog.close()
root.title('Viscosimetro')
es=[None]
ve=[None]
salir=Button(root,text="Salir",width=10,height=1,command=salir)
salir.pack(side=BOTTOM)
imgu = PhotoImage(file="ean.gif")
bar=Frame(root,bg='white',width=1000)
bar.pack()
bar1=Frame(bar,bg='white')
bar1.pack(side=RIGHT)
men1= Message(bar1,text="Universidad EAN\nFacultad de Ingenieria - Ingenieria Química",font=('arial',12,'bold'),bg="white",width=1000);
men1.pack(side=TOP)
lbl= Label(bar,image=imgu,bd=0);
lbl.pack()

master=LabelFrame(root,text="Viscosimetro",font=('arial',14,'bold'),width=1000,bg='white')
master.pack(side=BOTTOM)
usr= LabelFrame(master,text="Usuario",font=('arial',12),bg='white');
usr.pack(side=LEFT)
lbl1=Message(usr,text="Masa--------------------------",width=300,bg='white')
lbl1.pack()
mas = Entry(usr,width=7,bg='white')
mas.pack()
lbl1=Message(usr,text="Distancia---------------------",width=300,bg='white')
lbl1.pack()
dis = Entry(usr,width=7,bg='white')
dis.pack()
lbl1=Message(usr,text="Area---------------------",width=300,bg='white')
lbl1.pack()
are = Entry(usr,width=7,bg='white')
are.pack()
lbl1=Message(usr,text="Factor-------------------",width=300,bg='white')
lbl1.pack()
fac = Entry(usr,width=7,bg='white')
fac.pack()
barra=Frame(master,bg='white')
barra.pack(side= BOTTOM)
lbls=Message(barra,bg='white',text=" ")
lbls.pack()

salidas= LabelFrame(master,text="Entradas",font=('arial',12),bg='white');
salidas.pack(side=LEFT)
lbl2=Message(salidas, text="Tiempo------------------",width=300,bg='white')
lbl2.pack(side=TOP)
tim = Entry(salidas,width=15,bg='white')
tim.pack(side=TOP)
lbl3=Message(salidas, text="Temperatura------------------",width=300,bg='white')
lbl3.pack(side=TOP)
tmp = Entry(salidas,width=15,bg='white')
tmp.pack(side=TOP)

salidas= LabelFrame(master,text="Salidas",font=('arial',12),bg='white');
salidas.pack(side=LEFT)
lbl2=Message(salidas, text="Viscosidad------------------",width=300,bg='white')
lbl2.pack(side=TOP)
vis = Entry(salidas,width=15,bg='white')
vis.pack(side=TOP)
lbl3=Message(salidas, text="Esfuerzo Cortante-----------",width=300,bg='white')
lbl3.pack(side=TOP)
esf = Entry(salidas,width=15,bg='white')
esf.pack(side=TOP)
lbl3=Message(salidas, text="Velocidad-------------------",width=300,bg='white')
lbl3.pack(side=TOP)
vel = Entry(salidas,width=15,bg='white')
vel.pack(side=TOP)

def readSerial():
    while e.in_waiting:
        a=e.read()
        if a==b'n':
            tmp.delete(0,11)
            tim.delete(0,11)
            a=e.readline()
            b=e.read(5)
            tim.insert(1, a)
            tmp.insert(1, b)
            c=float(tim.get())/1000000
            print(c)
            tim.delete(0,11)
            tim.insert(1, c)
        calcu()
    root.after(10, readSerial)

def calcu():
    mu=(float(mas.get())*9.8*float(tim.get()))/(float(are.get())*float(dis.get()))*float(fac.get())
    print(mu)
    ta=(float(mas.get())*9.8)/float(are.get())
    print(ta)
    v=float(dis.get())/float(tim.get())
    print(v)
    vis.delete(0,40)
    esf.delete(0,40)
    vel.delete(0,40)
    vis.insert(1, mu)
    esf.insert(1, ta)
    vel.insert(1, v)
    es.append(ta)
    ve.append(v)
    flog=open('log.txt','a')
    tem=float(tmp.get())
    flog.write('\n'+str(v)+','+str(ta)+','+str(tem))
    flog.close()

def graf():
    plt.scatter(ve, es)
    plt.ylabel('Esfuerzo Cortante (N/m^2)')
    plt.xlabel('Velocidad (m/s)')
    plt.show()

gra=Button(salidas,text="Graficar",width=10,height=1,command=graf)
gra.pack()
root.after(10, readSerial)
root.update()
root.minsize(root.winfo_width(), root.winfo_height());
root.maxsize(root.winfo_width(), root.winfo_height());
root.mainloop();






