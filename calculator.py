# -*- coding:utf-8 -*-
import math
from tkinter import *
root = Tk()
root.title("Калькулятор комунальных услуг")
root.minsize(640, 320)
root.resizable(width=False, height=False)
frame = Frame(root)
frame.grid()

def inserter(value):
    output1.delete("0.0", "end")
    output1.insert("0.0", value)

def tarify(a1, b1, c1):
    water = a1 * 8.38
    text = "Счет за водоснабжение составляет: %s" % (water)
    if c1 <= 100:
        electric = c1*0.56
        text = "Счет за электричество составляет: %s" % (electric)
        return text
    elif c1>100:
        electric = c1*0.99
        text = "Счет за электричество составляет: %s" % (electric)
        return text
    if b1 <= 200:
        gas = b1*3.6
        text = "Счет за газ составляет: %s" % (gas)
        return text
    elif b1 > 200:
        gas = b1*7.188
        text = "Счет за газ составляет: %s" % (gas)
        return text
    return text
def handler():
    try:
        a_val = float(a.get())
        aa_val = float(aa.get())
        b_val = float(b.get())
        bb_val = float(bb.get())
        c_val = float(c.get())
        cc_val = float(cc.get())
        if aa_val > a_val:
            a1 = aa_val - a_val
            inserter(a1)
        if bb_val > b_val:
            b1 = bb_val - b_val

        if cc_val > c_val:
            c1 = cc_val - c_val

    except ValueError:
        inserter("НЕ работает")

a = Entry(frame, width=17)
aa = Entry(frame, width=17)
aa.grid(row=6, column=1, padx=(15, 0))
a.grid(row=4, column=1, padx=(15, 0))
a_lab = Label(frame, text="Вода", font="Arial 14").grid(row=1, column=1, padx=(15, 0))
a1_lab = Label(frame, text="Введите прошлые показания", font="Arial 9").grid(row=3, column=1, padx=(15, 0), pady=(30, 0))
a2_lab = Label(frame, text="Введите теперешние показания", font="Arial 9").grid(row=5, column=1, padx=(15, 0))
but1 = Button(frame, text="Посчитать", command=handler).grid(row=7, column=1)
output1 = Text(frame, bg="white", font="Arial 9", width=21, height=3)
output1.grid(row=8, column=1)

bb = Entry(frame, width=17)
b = Entry(frame, width=17)
bb.grid(row=6, column=2, padx=(15, 0))
b.grid(row=4, column=2, padx=(15, 0))
b_lab = Label(frame, text="Газ", font="Arial 14").grid(row=1, column=2, padx=(15, 0))
b1_lab = Label(frame, text="Введите прошлые показания", font="Arial 9").grid(row=3, column=2, padx=(15, 0), pady=(30, 0))
b2_lab = Label(frame, text="Введите теперешние показания", font="Arial 9").grid(row=5, column=2, padx=(15, 0))
but2 = Button(frame, text="Посчитать", command=handler).grid(row=7, column=2)
output2 = Text(frame, bg="white", font="Arial 9", width=21, height=3)
output2.grid(row=8, column=2)

c = Entry(frame, width=17)
cc = Entry(frame, width=17)
cc.grid(row=6, column=3, padx=(15, 0))
c.grid(row=4, column=3, padx=(15, 0))
c_lab = Label(frame, text="Электричество", font="Arial 14").grid(row=1, column=3, padx=(15, 0))
c1_lab = Label(frame, text="Введите прошлые показания", font="Arial 9").grid(row=3, column=3, padx=(15, 0), pady=(30, 0))
c2_lab = Label(frame, text="Введите теперешние показания", font="Arial 9").grid(row=5, column=3, padx=(15, 0))
but3 = Button(frame, text="Посчитать", command=handler).grid(row=7, column=3)
output3 = Text(frame, bg="white", font="Arial 9", width=21, height=3)
output3.grid(row=8, column=3)


# if aa_val > a_val:
#     a1 = aa_val - a_val
# if bb_val > b_val:
#     b1 = bb_val - b_val
# if cc_val > c_val:
#     c1 = cc_val - c_val


root.mainloop()