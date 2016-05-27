from tkinter import *

root = Tk()
logo = PhotoImage(file="icon1.gif")
w1 = Label(root, image=logo).pack(side="right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""
w2 = Label(root, 
           justify=LEFT,  #LEFT, RIGHT or CENTER
           padx = 10, 
           text=explanation).pack(side="left")
root.mainloop()
