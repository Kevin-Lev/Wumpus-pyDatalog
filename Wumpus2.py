from tkinter import *
from pyDatalog import *
from random import randint

mainframe = Tk()
mainframe.geometry("800x600+0+150")

frameTabuleiro = Frame(mainframe, height=410, width=410)
frameTabuleiro.place(x=50, y=50)

tabuleiro = Canvas(frameTabuleiro, bg="white", height=420, width=420)
tabuleiro.pack(fill=BOTH, expand=YES)

#1ª Linha
tabuleiro.create_rectangle(10,10,110,110, fill="white")
tabuleiro.create_rectangle(110,10,210,110, fill="white")
tabuleiro.create_rectangle(210,10,310,110, fill="white")
tabuleiro.create_rectangle(310,10,410,110, fill="white")

#2ª Linha
tabuleiro.create_rectangle(10,110,110,210, fill="white")
tabuleiro.create_rectangle(110,110,210,210, fill="white")
tabuleiro.create_rectangle(210,110,310,210, fill="white")
tabuleiro.create_rectangle(310,110,410,210, fill="white")

#3ª Linha
tabuleiro.create_rectangle(10,210,110,310, fill="white")
tabuleiro.create_rectangle(110,210,210,310, fill="white")
tabuleiro.create_rectangle(210,210,310,310, fill="white")
tabuleiro.create_rectangle(310,210,410,310, fill="white")

#4ª Linha
tabuleiro.create_rectangle(10,310,110,410, fill="white")
tabuleiro.create_rectangle(110,310,210,410, fill="white")
tabuleiro.create_rectangle(210,310,310,410, fill="white")
tabuleiro.create_rectangle(310,310,410,410, fill="white")

fotoCacador = PhotoImage(file="cacador-com-arco-e-flecha_318-53990.gif")
tabuleiro.create_image(60,380, image=fotoCacador)

buracoRetangulo = []
coordsBuraco1 = []
coordsBuraco2 = []
coordsBuraco3 = []

while(len(buracoRetangulo) < 3):
    num_random = randint(1,16)
    if((num_random != 13 and num_random != 14 and num_random != 9) and num_random not in buracoRetangulo):
        buracoRetangulo.append(num_random)

coordsBuraco1 = tabuleiro.coords(buracoRetangulo[0])
coordsBuraco2 = tabuleiro.coords(buracoRetangulo[1])
coordsBuraco3 = tabuleiro.coords(buracoRetangulo[2])


tabuleiro.create_oval(coordsBuraco1[0], coordsBuraco1[1], coordsBuraco1[2], coordsBuraco1[3], fill="black")
tabuleiro.create_text(coordsBuraco1[0]+50, coordsBuraco1[1]+50, text="SE FUDEU", fill="white")
tabuleiro.create_oval(coordsBuraco2[0], coordsBuraco2[1], coordsBuraco2[2], coordsBuraco2[3], fill="black")
tabuleiro.create_text(coordsBuraco2[0]+50, coordsBuraco2[1]+50, text="SE FUDEU", fill="white")
tabuleiro.create_oval(coordsBuraco3[0], coordsBuraco3[1], coordsBuraco3[2], coordsBuraco3[3], fill="black", state=HIDDEN)
tabuleiro.create_text(coordsBuraco3[0]+50, coordsBuraco3[1]+50, text="SE FUDEU", fill="white")

#fotoPit = PhotoImage(file="pit.gif")
#tabuleiro.create_image(60,260, image=fotoPit)

mainframe.mainloop()
