from tkinter import *
from calendar import isleap


def skaiciuoti():
    if isleap(sarasas[boksas.curselection()[0]]):
        pavadinimas['text'] = "Keliamieji"
    else:
        pavadinimas['text'] = "NEKeliamieji"


langas = Tk()
langas.title("Mano programa")
langas.iconbitmap(r'sveikinimas.ico')
langas.geometry("600x250")
antras = Frame(langas)
mygtukas1 = Button(langas, text="Skaičiuoti", command=skaiciuoti)
scrollbaras = Scrollbar(antras)
boksas = Listbox(antras, yscrollcommand=scrollbaras.set, selectmode=SINGLE)
pavadinimas = Label(langas, text="Laba diena")
scrollbaras.config(command=boksas.yview)
sarasas = range(1800, 2200)
boksas.insert(END, *sarasas)


antras.grid(row=0, column=0)
boksas.pack(side=LEFT)
mygtukas1.grid(row=0, column=1)
pavadinimas.grid(row=0, column=2)
scrollbaras.pack(side=RIGHT, fill=Y)
langas.mainloop()