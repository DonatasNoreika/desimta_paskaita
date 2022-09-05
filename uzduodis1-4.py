from tkinter import (Tk, Label, Entry,
                     Button, BOTTOM, TOP,
                     Menu, StringVar, SUNKEN, W, X)


def say_hello():
    name = entry1.get()
    greeting = f"Labas, {name}"
    last_text.set(greeting)
    res_label['text'] = greeting
    status["text"] = "Sukurta"

def clean():
    res_label['text'] = ""
    entry1.delete(0, "end")
    status["text"] = "Ištrinta"

def restore():
    res_label['text'] = last_text.get()
    status["text"] = "Atkurta"

def exit():
    window.quit()

window = Tk()
last_text = StringVar()
window.geometry("280x150")
window.title("Mano programa")
label1 = Label(window, text="Įveskite vardą")
entry1 = Entry(window)
button1 = Button(window, text="Įvesti", command=say_hello)
window.bind("<Return>", lambda e: say_hello())
res_label = Label(window)
status = Label(window, text="", bd=1, relief=SUNKEN, anchor=W)

menu = Menu(window)
window.config(menu=menu)
submenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Meniu", menu=submenu)
submenu.add_cascade(label="Išvalyti", command=clean)
submenu.add_cascade(label="Atkurti", command=restore)
submenu.add_separator()
submenu.add_cascade(label="Išeiti", command=exit)

label1.pack(side=TOP)
entry1.pack(side=TOP)
button1.pack(side=TOP)
res_label.pack(side=TOP)
status.pack(side=BOTTOM, fill=X)
window.mainloop()
