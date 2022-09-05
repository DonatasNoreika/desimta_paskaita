from tkinter import (Tk, Label, Entry,
                     Button, BOTTOM, TOP,
                     Menu, SUNKEN, W, X)

from calendar import isleap


def check():
    year = int(entry1.get())
    if isleap(year):
        res_label['text'] = "Keliamieji"
    else:
        res_label['text'] = "Nekeliamieji"
    entry1.delete(0, "end")

def exit():
    window.quit()

window = Tk()
window.geometry("280x150")
window.title("Ar keliamieji")
label1 = Label(window, text="Įveskite metus")
entry1 = Entry(window)
button1 = Button(window, text="Įvesti", command=check)
window.bind("<Return>", lambda e: check())
res_label = Label(window)

menu = Menu(window)
window.config(menu=menu)
submenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Meniu", menu=submenu)
submenu.add_separator()
submenu.add_cascade(label="Išeiti", command=exit)

label1.pack(side=TOP)
entry1.pack(side=TOP)
button1.pack(side=TOP)
res_label.pack(side=TOP)
window.mainloop()
