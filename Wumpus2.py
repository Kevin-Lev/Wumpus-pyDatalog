from tkinter import *
from pyDatalog import *

mainframe = Tk()
mainframe.geometry("800x600+0+150")

frameTabuleiro = Frame(mainframe, height=410, width=410)
frameTabuleiro.place(x=50, y=50)

tabuleiro = Canvas(frameTabuleiro, bg="blue", height=420, width=420)
tabuleiro.pack(fill=BOTH, expand=YES)

#1ª Linha
tabuleiro.create_rectangle(10,10,110,110, fill="blue")
tabuleiro.create_rectangle(110,10,210,110, fill="gray")
tabuleiro.create_rectangle(210,10,310,110, fill="blue")
tabuleiro.create_rectangle(310,10,410,110, fill="gray")

#2ª Linha
tabuleiro.create_rectangle(10,110,110,210, fill="gray")
tabuleiro.create_rectangle(110,110,210,210, fill="blue")
tabuleiro.create_rectangle(210,110,310,210, fill="gray")
tabuleiro.create_rectangle(310,110,410,210, fill="blue")

#3ª Linha
tabuleiro.create_rectangle(10,210,110,310, fill="blue")
tabuleiro.create_rectangle(110,210,210,310, fill="gray")
tabuleiro.create_rectangle(210,210,310,310, fill="blue")
tabuleiro.create_rectangle(310,210,410,310, fill="gray")

#4ª Linha
tabuleiro.create_rectangle(10,310,110,410, fill="gray")
tabuleiro.create_rectangle(110,310,210,410, fill="blue")
tabuleiro.create_rectangle(210,310,310,410, fill="gray")
tabuleiro.create_rectangle(310,310,410,410, fill="blue")

mainframe.mainloop()
