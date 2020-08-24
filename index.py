
from tkinter import*
cuadro =Tk()

var = StringVar()
cuadro.geometry("600x500")
cuadro =Frame(cuadro, width=1200, height=600)
cuadro.grid()
calif1=Entry(cuadro)
calif1.grid(row=0, column=1)
calif1=Label(cuadro, text="calificacion 1:")

calif1.grid(row=0, column=0)
calif2=Entry(cuadro,)
calif2.grid(row=1, column=1)

calif2=Label(cuadro, text="calificacion 2:")
calif2.grid(row=1, column=0)

calif3=Entry(cuadro,)
calif3.grid(row=2, column=1)
calif3=Label(cuadro, text="calificacion 3:")
calif3.grid(row=2, column=0)
examF=Entry(cuadro,)
examF.grid(row=3, column=1)
examF=Label(cuadro, text="exame final:")
examF.grid(row=3, column=0)
trabF=Entry(cuadro,)
trabF.grid(row=4, column=1)
trabF=Label(cuadro, text="trabajo final")
trabF.grid(row=4, column=0)

resultado=Label(cuadro, textvariable=var)
resultado.grid()

def nota():
    nota = a = float(calif1.get()) + float(calif2.get()) + float(calif2.get()) + float(calif3.get()) / float(3)*float(0.55)
    nota = b = float(examF.get())*float(0.30)
    nota = c =float(trabF.get()) +float(0.15)
    nota=  float(a)+float(b)+float(c)
    return var.set(nota)


button=Button(cuadro, text="click", command=nota)
button.grid()

cuadro.mainloop()

