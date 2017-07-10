from tkinter import *
from pyDatalog import pyDatalog
from random import randint

pyDatalog.create_terms('tem_poco, tem_brisa, tem_wumpus, tem_fedor, tem_ouro, tem_brilho')
pyDatalog.create_terms('linha, coluna')
pyDatalog.create_terms('andar, casa_jogador, status')
pyDatalog.create_terms('X, Y')

# BASE DE LINHAS
# linha[X] == Y significa a casa X está na linha Y
+ (linha[1] == 1)
+ (linha[2] == 1)
+ (linha[3] == 1)
+ (linha[4] == 1)
+ (linha[5] == 2)
+ (linha[6] == 2)
+ (linha[7] == 2)
+ (linha[8] == 2)
+ (linha[9] == 3)
+ (linha[10] == 3)
+ (linha[11] == 3)
+ (linha[12] == 3)
+ (linha[13] == 4)
+ (linha[14] == 4)
+ (linha[15] == 4)
+ (linha[16] == 4)

# BASE DE COLUNAS
# coluna[X] == Y significa que a casa X está na coluna Y
+ (coluna[1] == 1)
+ (coluna[2] == 2)
+ (coluna[3] == 3)
+ (coluna[4] == 4)
+ (coluna[5] == 1)
+ (coluna[6] == 2)
+ (coluna[7] == 3)
+ (coluna[8] == 4)
+ (coluna[9] == 1)
+ (coluna[10] == 2)
+ (coluna[11] == 3)
+ (coluna[12] == 4)
+ (coluna[13] == 1)
+ (coluna[14] == 2)
+ (coluna[15] == 3)
+ (coluna[16] == 4)

# BASE OURO BRILHO
tem_brilho(X) <= tem_ouro(X)

# BASE FEDOR WUMPUS
tem_fedor(1) <= tem_wumpus(2)
tem_fedor(1) <= tem_wumpus(5)
tem_fedor(2) <= tem_wumpus(1)
tem_fedor(2) <= tem_wumpus(6)
tem_fedor(2) <= tem_wumpus(3)
tem_fedor(3) <= tem_wumpus(2)
tem_fedor(3) <= tem_wumpus(7)
tem_fedor(3) <= tem_wumpus(4)
tem_fedor(4) <= tem_wumpus(3)
tem_fedor(4) <= tem_wumpus(8)
tem_fedor(5) <= tem_wumpus(1)
tem_fedor(5) <= tem_wumpus(6)
tem_fedor(5) <= tem_wumpus(9)
tem_fedor(6) <= tem_wumpus(2)
tem_fedor(6) <= tem_wumpus(5)
tem_fedor(6) <= tem_wumpus(7)
tem_fedor(6) <= tem_wumpus(10)
tem_fedor(7) <= tem_wumpus(3)
tem_fedor(7) <= tem_wumpus(6)
tem_fedor(7) <= tem_wumpus(8)
tem_fedor(7) <= tem_wumpus(11)
tem_fedor(8) <= tem_wumpus(4)
tem_fedor(8) <= tem_wumpus(7)
tem_fedor(8) <= tem_wumpus(12)
tem_fedor(9) <= tem_wumpus(5)
tem_fedor(9) <= tem_wumpus(10)
tem_fedor(9) <= tem_wumpus(13)
tem_fedor(10) <= tem_wumpus(6)
tem_fedor(10) <= tem_wumpus(9)
tem_fedor(10) <= tem_wumpus(11)
tem_fedor(10) <= tem_wumpus(14)
tem_fedor(11) <= tem_wumpus(7)
tem_fedor(11) <= tem_wumpus(10)
tem_fedor(11) <= tem_wumpus(12)
tem_fedor(11) <= tem_wumpus(15)
tem_fedor(12) <= tem_wumpus(8)
tem_fedor(12) <= tem_wumpus(11)
tem_fedor(12) <= tem_wumpus(16)
tem_fedor(13) <= tem_wumpus(9)
tem_fedor(13) <= tem_wumpus(14)
tem_fedor(14) <= tem_wumpus(10)
tem_fedor(14) <= tem_wumpus(13)
tem_fedor(14) <= tem_wumpus(15)
tem_fedor(15) <= tem_wumpus(11)
tem_fedor(15) <= tem_wumpus(14)
tem_fedor(15) <= tem_wumpus(16)
tem_fedor(16) <= tem_wumpus(12)
tem_fedor(16) <= tem_wumpus(15)

# BASE BRISA POÇO
tem_brisa(1) <= tem_poco(2)
tem_brisa(1) <= tem_poco(5)
tem_brisa(2) <= tem_poco(1)
tem_brisa(2) <= tem_poco(6)
tem_brisa(2) <= tem_poco(3)
tem_brisa(3) <= tem_poco(2)
tem_brisa(3) <= tem_poco(7)
tem_brisa(3) <= tem_poco(4)
tem_brisa(4) <= tem_poco(3)
tem_brisa(4) <= tem_poco(8)
tem_brisa(5) <= tem_poco(1)
tem_brisa(5) <= tem_poco(6)
tem_brisa(5) <= tem_poco(9)
tem_brisa(6) <= tem_poco(2)
tem_brisa(6) <= tem_poco(5)
tem_brisa(6) <= tem_poco(7)
tem_brisa(6) <= tem_poco(10)
tem_brisa(7) <= tem_poco(3)
tem_brisa(7) <= tem_poco(6)
tem_brisa(7) <= tem_poco(8)
tem_brisa(7) <= tem_poco(11)
tem_brisa(8) <= tem_poco(4)
tem_brisa(8) <= tem_poco(7)
tem_brisa(8) <= tem_poco(12)
tem_brisa(9) <= tem_poco(5)
tem_brisa(9) <= tem_poco(10)
tem_brisa(9) <= tem_poco(13)
tem_brisa(10) <= tem_poco(6)
tem_brisa(10) <= tem_poco(9)
tem_brisa(10) <= tem_poco(11)
tem_brisa(10) <= tem_poco(14)
tem_brisa(11) <= tem_poco(7)
tem_brisa(11) <= tem_poco(10)
tem_brisa(11) <= tem_poco(12)
tem_brisa(11) <= tem_poco(15)
tem_brisa(12) <= tem_poco(8)
tem_brisa(12) <= tem_poco(11)
tem_brisa(12) <= tem_poco(16)
tem_brisa(13) <= tem_poco(9)
tem_brisa(13) <= tem_poco(14)
tem_brisa(14) <= tem_poco(10)
tem_brisa(14) <= tem_poco(13)
tem_brisa(14) <= tem_poco(15)
tem_brisa(15) <= tem_poco(11)
tem_brisa(15) <= tem_poco(14)
tem_brisa(15) <= tem_poco(16)
tem_brisa(16) <= tem_poco(12)
tem_brisa(16) <= tem_poco(15)

# BASE PARA STATUS DO JOGO
status['morreu'] == False
(status['morreu'] == True) <= (casa_jogador(X) & tem_wumpus(X))
(status['morreu'] == True) <= (casa_jogador(X) & tem_poco(X))
status['venceu'] == False
(status['venceu'] == True) <= (casa_jogador(13) & (status['pegou_ouro'] == True))
status['fim_jogo'] == False
(status['fim_jogo'] == True) <= (status['venceu'] == True)
(status['fim_jogo'] == True) <= (status['morreu'] == True)

mainframe = Tk()
mainframe.geometry("800x600+0+150")

frameTabuleiro = Frame(mainframe, height=410, width=410)
frameTabuleiro.place(x=50, y=50)

tabuleiro = Canvas(frameTabuleiro, bg="black", height=420, width=420)
tabuleiro.pack(fill=BOTH, expand=YES)


buracoRetangulo = []
coordsBuraco1 = []
coordsBuraco2 = []
coordsBuraco3 = []
WumpusRetangulo = {}
coordsWumpus = []
tesouroWumpus = {}
coordsTesouro = []
coordsCacador = []
Pirata = {}

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

def leftKey(event):
    global Pirata, coordsCacador
    tabuleiro.delete(Pirata)
    Pirata = tabuleiro.create_image(coordsCacador[0]-100,coordsCacador[1], image=fotoCacador)
    coordsCacador = tabuleiro.coords(Pirata)
    print("Seta esquerda pressionada")

def rightKey(event):
    global Pirata, coordsCacador
    tabuleiro.delete(Pirata)
    Pirata = tabuleiro.create_image(coordsCacador[0]+100,coordsCacador[1], image=fotoCacador)
    coordsCacador = tabuleiro.coords(Pirata)
    print("Seta direita pressionada")

def upKey(event):
    global Pirata, coordsCacador
    tabuleiro.delete(Pirata)
    Pirata = tabuleiro.create_image(coordsCacador[0],coordsCacador[1]-100, image=fotoCacador)
    coordsCacador = tabuleiro.coords(Pirata)
    print("Seta para cima pressionada")

def downKey(event):
    global Pirata, coordsCacador
    tabuleiro.delete(Pirata)
    Pirata = tabuleiro.create_image(coordsCacador[0],coordsCacador[1]+100, image=fotoCacador)
    coordsCacador = tabuleiro.coords(Pirata)
    print("Seta para baixo pressionada")


fotoCacador = PhotoImage(file="pirata.gif")
Pirata = tabuleiro.create_image(60,370, image=fotoCacador)
coordsCacador = tabuleiro.coords(Pirata)

fotoWumpus = PhotoImage(file="wumpus_small.gif")
fotoTesouro = PhotoImage(file="0.gif")

def paraEsquerda(self):
    if(coordsCacador[0] > 110):
        leftKey(self)
    else:
        print("Não é possível ir para a esquerda !!")

def paraDireita(self):
    if(coordsCacador[0] < 310):
        rightKey(self)
    else:
        print("Não é possível ir para a direita !!")

def paraCima(self):
    if(coordsCacador[1] > 110):
        upKey(self)
    else:
        print("Não é possível ir para cima !!")

def paraBaixo(self):
    if(coordsCacador[1] < 310):
        downKey(self)
    else:
        print("Não é possível ir para baixo !!")

def getRetangulo(self, pirataX, pirataY):
    if(pirataX == 60 and pirataY == 70):
        return 1
    elif(pirataX == 160 and pirataY == 70):
        return 2
    elif(pirataX == 260 and pirataY == 70):
        return 3
    elif(pirataX == 360 and pirataY == 70):
        return 4
    elif(pirataX == 60 and pirataY == 170):
        return 5
    elif(pirataX == 160 and pirataY == 170):
        return 6
    elif(pirataX == 260 and pirataY == 170):
        return 7
    elif(pirataX == 360 and pirataY == 170):
        return 8
    elif(pirataX == 60 and pirataY == 270):
        return 9
    elif(pirataX == 160 and pirataY == 270):
        return 10
    elif(pirataX == 260 and pirataY == 270):
        return 11
    elif(pirataX == 360 and pirataY == 270):
        return 12
    elif(pirataX == 60 and pirataY == 370):
        return 13
    elif(pirataX == 160 and pirataY == 370):
        return 14
    elif(pirataX == 260 and pirataY == 370):
        return 15
    else:
        return 16


def

def bangCima(self):
    print("atirou para cima!")
    idRetangulo = getRetangulo(self, coordsCacador[0], coordsCacador[1])
    print(idRetangulo)


def bangBaixo(self):
    print("Atirou para baixo!")

def bangEsquerda(self):
    print("Atirou para a esquerda!")

def bangDireita(self):
    print("Atirou para a direita!")


while(len(buracoRetangulo) < 3):
    num_random = randint(1,16)
    if((num_random != 13 and num_random != 14 and num_random != 9) and num_random not in buracoRetangulo):
        buracoRetangulo.append(num_random)

while(True):
    num_random = randint(1,16)
    if((num_random != 13 and num_random != 14 and num_random != 9) and num_random not in buracoRetangulo):
        WumpusRetangulo = num_random
        break

while(True):
    num_random = randint(1,16)
    if((num_random != 13 and num_random != 14 and num_random != 9) and num_random not in buracoRetangulo and num_random != WumpusRetangulo):
        tesouroWumpus = num_random
        break

coordsBuraco1 = tabuleiro.coords(buracoRetangulo[0])
coordsBuraco2 = tabuleiro.coords(buracoRetangulo[1])
coordsBuraco3 = tabuleiro.coords(buracoRetangulo[2])
coordsWumpus = tabuleiro.coords(WumpusRetangulo)
coordsTesouro = tabuleiro.coords(tesouroWumpus)

tabuleiro.create_oval(coordsBuraco1[0], coordsBuraco1[1], coordsBuraco1[2], coordsBuraco1[3], fill="black")
tabuleiro.create_text(coordsBuraco1[0]+50, coordsBuraco1[1]+50, text="SE FUDEU", fill="white")
tabuleiro.create_oval(coordsBuraco2[0], coordsBuraco2[1], coordsBuraco2[2], coordsBuraco2[3], fill="black")
tabuleiro.create_text(coordsBuraco2[0]+50, coordsBuraco2[1]+50, text="SE FUDEU", fill="white")
tabuleiro.create_oval(coordsBuraco3[0], coordsBuraco3[1], coordsBuraco3[2], coordsBuraco3[3], fill="black", state=HIDDEN)
tabuleiro.create_text(coordsBuraco3[0]+50, coordsBuraco3[1]+50, text="SE FUDEU", fill="white")
tabuleiro.create_image(coordsWumpus[0]+50, coordsWumpus[1]+50, image=fotoWumpus)
tabuleiro.create_image(coordsTesouro[0]+50, coordsTesouro[1]+50, image=fotoTesouro)


tabuleiro.bind('<Left>', paraEsquerda)
tabuleiro.bind('<Right>', paraDireita)
tabuleiro.bind('<Up>', paraCima)
tabuleiro.bind('<Down>', paraBaixo)
tabuleiro.bind('<Control-Key-Up>', bangCima)
tabuleiro.bind('<Control-Key-Down>', bangBaixo)
tabuleiro.bind('<Control-Key-Left>', bangEsquerda)
tabuleiro.bind('<Control-Key-Right>', bangDireita)
tabuleiro.focus_set()

mainloop()
