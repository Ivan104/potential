# -*- coding:utf-8 -*-
import math
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Калькулятор комунальных послуг")
root.minsize(630, 320)
root.resizable(width=False, height=False)
frame = Frame(root)
frame.grid()

water_score = 8.38
electric1_score = 0.56
electric2_score = 0.99
gas1_score = 3.6
gas2_score = 7.188

def tarify_water(a1, a2):
    if a1 < a2:
        val1 = abs(a1 - a2)
        water = val1 * water_score
        text = "Рахунок за водопостачання  становить: %.2f %s" % (water, "грн")
        return text
def tarify_electric(c1, c2):
    if c1 < c2:
        val2 = abs(c1 - c2)
        if val2 <= 100:
            electric = val2 * electric1_score
            text = "Рахунок за електрику становить: %.2f %s" % (electric, "грн")
            return text
        elif val2 > 100:
            electric = val2 * electric2_score
            text = "Рахунок за електрику становить: %.2f %s" % (electric, "грн")
            return text
def tarify_gas(b1, b2):
    if b1 < b2:
        val3 = abs(b1 - b2)
        if val3 <= 200:
            gas = val3 * gas1_score
            text = "Рахунок за газ становить: %.2f %s" % (gas, "грн")
            return text
        elif val3 > 200:
            gas = val3 * gas2_score
            text = "Рахунок за газ становить: %.2f %s" % (gas, "грн")
            return text

def handler1():
    try:
        a_val = float(a.get())
        aa_val = float(aa.get())
        inserter1(tarify_water(a_val, aa_val))
    except ValueError:
        inserter1("Не правильно введені дані")

def handler2():
    try:
        b_val = float(b.get())
        bb_val = float(bb.get())
        inserter2(tarify_gas(b_val, bb_val))
    except ValueError:
        inserter2("Не правильно введені дані")

def handler3():
    try:
        c_val = float(c.get())
        cc_val = float(cc.get())
        inserter3(tarify_electric(c_val, cc_val))
    except ValueError:
        inserter3("Не правильно введені дані")

def clear(event):
    caller = event.widget
    caller.delete("0", "end")

a = Entry(frame, width=17)
aa = Entry(frame, width=17)
a.bind("<FocusIn>", clear)
aa.bind("<FocusIn>", clear)
aa.grid(row=6, column=1, padx=(15, 0))
a.grid(row=4, column=1, padx=(15, 0))
a_lab = Label(frame, text="Вода", font="Arial 14").grid(row=1, column=1, padx=(15, 0))
a1_lab = Label(frame, text="Минулі показники лічильника", font="Arial 9").grid(row=3, column=1, padx=(15, 0), pady=(30, 0))
a2_lab = Label(frame, text="Теперішні показники лічильника", font="Arial 9").grid(row=5, column=1, padx=(15, 0))
but1 = Button(frame, text="Порахувати", command=handler1).grid(row=7, column=1)
output1 = Text(frame, bg="white", font="Arial 9", width=20, height=3, padx=(5))
output1.grid(row=8, column=1)

bb = Entry(frame, width=17)
b = Entry(frame, width=17)
b.bind("<FocusIn>", clear)
bb.bind("<FocusIn>", clear)
bb.grid(row=6, column=2, padx=(15, 0))
b.grid(row=4, column=2, padx=(15, 0))
b_lab = Label(frame, text="Газ", font="Arial 14").grid(row=1, column=2, padx=(15, 0))
b1_lab = Label(frame, text="Минулі показники лічильника", font="Arial 9").grid(row=3, column=2, padx=(15, 0), pady=(30, 0))
b2_lab = Label(frame, text="Теперішні показники лічильника", font="Arial 9").grid(row=5, column=2, padx=(15, 0))
but2 = Button(frame, text="Порахувати", command=handler2).grid(row=7, column=2)
output2 = Text(frame, bg="white", font="Arial 9", width=20, height=3, padx=(5))
output2.grid(row=8, column=2)

c = Entry(frame, width=17)
cc = Entry(frame, width=17)
c.bind("<FocusIn>", clear)
cc.bind("<FocusIn>", clear)
cc.grid(row=6, column=3, padx=(15, 0))
c.grid(row=4, column=3, padx=(15, 0))
c_lab = Label(frame, text="Електрика", font="Arial 14").grid(row=1, column=3, padx=(15, 0))
c1_lab = Label(frame, text="Минулі показники лічильника", font="Arial 9").grid(row=3, column=3, padx=(15, 0), pady=(30, 0))
c2_lab = Label(frame, text="Теперішні показники лічильника", font="Arial 9").grid(row=5, column=3, padx=(15, 0))
but3 = Button(frame, text="Порахувати", command=handler3).grid(row=7, column=3)
output3 = Text(frame, bg="white", font="Arial 9", width=20, height=3, padx=(5))
output3.grid(row=8, column=3)

def inserter1(value1):
    output1.delete('0.0', 'end')
    output1.insert('0.0', value1)

def inserter2(value2):
    output2.delete('0.0', 'end')
    output2.insert('0.0', value2)

def inserter3(value3):
    output3.delete('0.0', 'end')
    output3.insert('0.0', value3)

def on_closing():
    if messagebox.askokcancel("Вийти", "Ви справді хочете завершити роботу?"):
        root.destroy()

def about():
    messagebox.showinfo('Про програму', 'Калькулятор комунальных послуг \n Версія 0.1 \n Кожен може експлуатувати дану програму \n\n З будь-яких питань і пропозицій звертайтесь поштою: ivankovalenko104@gmail.com ')

root.protocol("WM_DELETE_WINDOW", on_closing)

# def settings():
#     global water_score
#     global electric1_score
#     global electric2_score
#     global gas1_score
#     global gas2_score
#     settingsDialog = Frame(root, water_score=water_score, electric1_score=electric1_score, electric2_score=electric2_score, gas1_score=gas1_score, gas2_score=gas2_score)
#     root.wait_window(settingsDialog.top)
#     water_score = settingsDialog.water_score
#     electric1_score = settingsDialog.electric1_score
#     electric2_score = settingsDialog.electric2_score
#     gas1_score = settingsDialog.gas1_score
#     gas2_score = settingsDialog.gas2_score

#Создание диалогого меню
menu = Menu(root)
root.config(menu=menu)
meFile = Menu(menu)
menu.add_cascade(label="Меню", menu=meFile)
meFile.add_command(label="Істория")
meFile.add_separator()
meFile.add_command(label="Вихід", command=root.quit)

meEdit = Menu(menu)
menu.add_cascade(label="Налаштування", menu=meEdit)
meEdit.add_command(label="Тарифи",)

meHelp = Menu(menu)
menu.add_cascade(label="Довідка", menu=meHelp)
meHelp.add_command(label="Про програму", command=about)


root.mainloop()