from tkinter import *
from pyDatalog import pyDatalog
from random import randint
import random
import os
from operator import itemgetter

pyDatalog.create_terms('tem_poco, tem_brisa, tem_wumpus, tem_fedor, tem_ouro, tem_brilho')
pyDatalog.create_terms('linha, coluna')
pyDatalog.create_terms('casa_jogador')
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

mainframe = Tk()
mainframe.geometry("800x500+0+150")
mainframe.wm_title("Wumpus Game")

frameTabuleiro = Frame(mainframe, height=410, width=410)
frameTabuleiro.place(x=50, y=50)

tabuleiro = Canvas(frameTabuleiro, bg="black", height=420, width=420)
tabuleiro.pack(fill=BOTH, expand=YES)

textoJogo = Text(mainframe, height=30, width=40, bg="black", fg="white")
textoJogo.place(x=500, y=50)

labelInfo = Label(mainframe, text="Game Info")
labelInfo.place(x=500, y=30)

janelaFim = Tk()
janelaFim.geometry("180x120+350+300")
janelaFim.withdraw()

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
linhaColunaRet = {}

# 1ª Linha
tabuleiro.create_rectangle(10, 10, 110, 110, fill="white")
tabuleiro.create_rectangle(110, 10, 210, 110, fill="white")
tabuleiro.create_rectangle(210, 10, 310, 110, fill="white")
tabuleiro.create_rectangle(310, 10, 410, 110, fill="white")

# 2ª Linha
tabuleiro.create_rectangle(10, 110, 110, 210, fill="white")
tabuleiro.create_rectangle(110, 110, 210, 210, fill="white")
tabuleiro.create_rectangle(210, 110, 310, 210, fill="white")
tabuleiro.create_rectangle(310, 110, 410, 210, fill="white")

# 3ª Linha
tabuleiro.create_rectangle(10, 210, 110, 310, fill="white")
tabuleiro.create_rectangle(110, 210, 210, 310, fill="white")
tabuleiro.create_rectangle(210, 210, 310, 310, fill="white")
tabuleiro.create_rectangle(310, 210, 410, 310, fill="white")

# 4ª Linha
tabuleiro.create_rectangle(10, 310, 110, 410, fill="white")
tabuleiro.create_rectangle(110, 310, 210, 410, fill="white")
tabuleiro.create_rectangle(210, 310, 310, 410, fill="white")
tabuleiro.create_rectangle(310, 310, 410, 410, fill="white")


def verificaNovaCasa(event):
    casaJogador = getRetangulo(event, coordsCacador[0], coordsCacador[1])
    + casa_jogador(casaJogador)
    fedorNaCasa(casaJogador)
    brisaNaCasa(casaJogador)
    brilhoNaCasa(casaJogador)
    fimDeJogo(casaJogador)
    textoJogo.insert(END, "\n- - - - - - - - -\n")


def leftKey(event):
    global Pirata, coordsCacador
    tabuleiro.delete(Pirata)
    - casa_jogador(getRetangulo(event, coordsCacador[0], coordsCacador[1]))
    Pirata = tabuleiro.create_image(coordsCacador[0] - 100, coordsCacador[1], image=fotoCacador)
    coordsCacador = tabuleiro.coords(Pirata)
    verificaNovaCasa(event)
    print("Seta esquerda pressionada")


def rightKey(event):
    global Pirata, coordsCacador
    tabuleiro.delete(Pirata)
    - casa_jogador(getRetangulo(event, coordsCacador[0], coordsCacador[1]))
    Pirata = tabuleiro.create_image(coordsCacador[0] + 100, coordsCacador[1], image=fotoCacador)
    coordsCacador = tabuleiro.coords(Pirata)
    verificaNovaCasa(event)
    print("Seta direita pressionada")


def upKey(event):
    global Pirata, coordsCacador
    tabuleiro.delete(Pirata)
    - casa_jogador(getRetangulo(event, coordsCacador[0], coordsCacador[1]))
    Pirata = tabuleiro.create_image(coordsCacador[0], coordsCacador[1] - 100, image=fotoCacador)
    coordsCacador = tabuleiro.coords(Pirata)
    verificaNovaCasa(event)
    print("Seta para cima pressionada")


def downKey(event):
    global Pirata, coordsCacador
    tabuleiro.delete(Pirata)
    - casa_jogador(getRetangulo(event, coordsCacador[0], coordsCacador[1]))
    Pirata = tabuleiro.create_image(coordsCacador[0], coordsCacador[1] + 100, image=fotoCacador)
    coordsCacador = tabuleiro.coords(Pirata)
    verificaNovaCasa(event)
    print("Seta para baixo pressionada")


fotoCacador = PhotoImage(file="pirata.gif")
Pirata = tabuleiro.create_image(60, 370, image=fotoCacador)
coordsCacador = tabuleiro.coords(Pirata)
+ casa_jogador(13)

fotoWumpus = PhotoImage(file="wumpus_small.gif")
fotoTesouro = PhotoImage(file="0.gif")


def paraEsquerda(self):
    if (coordsCacador[0] > 110):
        leftKey(self)
    else:
        print("Não é possível ir para a esquerda !!")


def paraDireita(self):
    if (coordsCacador[0] < 310):
        rightKey(self)
    else:
        print("Não é possível ir para a direita !!")


def paraCima(self):
    if (coordsCacador[1] > 110):
        upKey(self)
    else:
        print("Não é possível ir para cima !!")


def paraBaixo(self):
    if (coordsCacador[1] < 310):
        downKey(self)
    else:
        print("Não é possível ir para baixo !!")


def getRetangulo(self, pirataX, pirataY):
    if (pirataX == 60 and pirataY == 70):
        return 1
    elif (pirataX == 160 and pirataY == 70):
        return 2
    elif (pirataX == 260 and pirataY == 70):
        return 3
    elif (pirataX == 360 and pirataY == 70):
        return 4
    elif (pirataX == 60 and pirataY == 170):
        return 5
    elif (pirataX == 160 and pirataY == 170):
        return 6
    elif (pirataX == 260 and pirataY == 170):
        return 7
    elif (pirataX == 360 and pirataY == 170):
        return 8
    elif (pirataX == 60 and pirataY == 270):
        return 9
    elif (pirataX == 160 and pirataY == 270):
        return 10
    elif (pirataX == 260 and pirataY == 270):
        return 11
    elif (pirataX == 360 and pirataY == 270):
        return 12
    elif (pirataX == 60 and pirataY == 370):
        return 13
    elif (pirataX == 160 and pirataY == 370):
        return 14
    elif (pirataX == 260 and pirataY == 370):
        return 15
    else:
        return 16


def Reset():
    janelaFim.destroy()
    mainframe.destroy()
    os.system("python3.5 Wumpus2.py")
    #os.system("python Wumpus2.py")


def Exit():
    janelaFim.destroy()
    mainframe.destroy()


def fimDeJogo(casaJogador):
    global wumpusVivo, Pirata
    # if not(pyDatalog.ask('tem_wumpus(X)')==None) and not(pyDatalog.ask('tem_wumpus(X)')==None):
    wumpus = pyDatalog.ask('tem_wumpus(X)').answers
    poco = pyDatalog.ask('tem_poco(X)').answers
    if((pegouOuro == 1) and (casaJogador == 13)):
        janelaFim.wm_title("Você venceu!")
        janelaFim.deiconify()
        labelFim = Label(janelaFim, text="Você venceu!!\n\nDeseja jogar novamente?")
        labelFim.place(x=10, y=10)
        botaoSim = Button(janelaFim, text="Sim", command=Reset)
        botaoSim.place(x=30, y=70)
        botaoNao = Button(janelaFim, text="Não", command=Exit)
        botaoNao.place(x=100, y=70)
        return True
    if ((wumpus[0][0] == casaJogador) and wumpusVivo) or (poco[0][0] == casaJogador) or (poco[1][0] == casaJogador) or (
                poco[2][0] == casaJogador):
        janelaFim.wm_title("Game Over")
        janelaFim.deiconify()
        labelFim = Label(janelaFim, text="Game Over!\n\nDeseja jogar novamente?")
        labelFim.place(x=10, y=10)
        botaoSim = Button(janelaFim, text="Sim", command=Reset)
        botaoSim.place(x=30, y=70)
        botaoNao = Button(janelaFim, text="Não", command=Exit)
        botaoNao.place(x=100, y=70)
        tabuleiro.delete(Pirata)
        desenhaObstaculos()
        return True
    return False


def fedorNaCasa(casaJogador):
    listaFedor = pyDatalog.ask('tem_fedor(X)').answers
    for i in listaFedor:
        if i[0] == casaJogador:
            textoJogo.insert(END, "Fedor! ")
            return True
    return False


def brisaNaCasa(casaJogador):
    listaBrisa = pyDatalog.ask('tem_brisa(X)').answers
    for i in listaBrisa:
        if i[0] == casaJogador:
            textoJogo.insert(END, "Brisa! ")
            return True
    return False


def brilhoNaCasa(casaJogador):
    global pegouOuro
    if pegouOuro == 0:
        casaBrilho = pyDatalog.ask('tem_ouro(X)').answers
        if (casaBrilho[0][0] == casaJogador):
            textoJogo.insert(END, "Brilho! ")


def getLinhaColuna(self, idRet):
    if (idRet == 1):
        pi = pyDatalog.ask('linha[1] == X')
        pi2 = pyDatalog.ask('coluna[1] == X')
    elif (idRet == 2):
        pi = pyDatalog.ask('linha[2] == X')
        pi2 = pyDatalog.ask('coluna[2] == X')
    elif (idRet == 3):
        pi = pyDatalog.ask('linha[3] == X')
        pi2 = pyDatalog.ask('coluna[3] == X')
    elif (idRet == 4):
        pi = pyDatalog.ask('linha[4] == X')
        pi2 = pyDatalog.ask('coluna[4] == X')
    elif (idRet == 5):
        pi = pyDatalog.ask('linha[5] == X')
        pi2 = pyDatalog.ask('coluna[5] == X')
    elif (idRet == 6):
        pi = pyDatalog.ask('linha[6] == X')
        pi2 = pyDatalog.ask('coluna[6] == X')
    elif (idRet == 7):
        pi = pyDatalog.ask('linha[7] == X')
        pi2 = pyDatalog.ask('coluna[7] == X')
    elif (idRet == 8):
        pi = pyDatalog.ask('linha[8] == X')
        pi2 = pyDatalog.ask('coluna[8] == X')
    elif (idRet == 9):
        pi = pyDatalog.ask('linha[9] == X')
        pi2 = pyDatalog.ask('coluna[9] == X')
    elif (idRet == 10):
        pi = pyDatalog.ask('linha[10] == X')
        pi2 = pyDatalog.ask('coluna[10] == X')
    elif (idRet == 11):
        pi = pyDatalog.ask('linha[11] == X')
        pi2 = pyDatalog.ask('coluna[11] == X')
    elif (idRet == 12):
        pi = pyDatalog.ask('linha[12] == X')
        pi2 = pyDatalog.ask('coluna[12] == X')
    elif (idRet == 13):
        pi = pyDatalog.ask('linha[13] == X')
        pi2 = pyDatalog.ask('coluna[13] == X')
    elif (idRet == 14):
        pi = pyDatalog.ask('linha[14] == X')
        pi2 = pyDatalog.ask('coluna[14] == X')
    elif (idRet == 15):
        pi = pyDatalog.ask('linha[15] == X')
        pi2 = pyDatalog.ask('coluna[15] == X')
    else:
        pi = pyDatalog.ask('linha[16] == X')
        pi2 = pyDatalog.ask('coluna[16] == X')

    return pi, pi2


tiros = 1
wumpusVivo = True


def atirarFlecha(self, casaJogador, direcao):  # 0: esq; 1: cima; 2: dir; 3: baixo
    global tiros, wumpusVivo
    if (tiros > 0):
        wumpus = pyDatalog.ask('tem_wumpus(X)').answers
        linhaWumpus, colunaWumpus = getLinhaColuna(self, wumpus[0][0])
        linhaJogador, colunaJogador = getLinhaColuna(self, casaJogador)
        if direcao == 0:
            if (linhaWumpus == linhaJogador) and (wumpus[0][0] < casaJogador):
                textoJogo.insert(END, "Você matou o wumpus!\n")
                - tem_wumpus(casaJogador)
                wumpusVivo = False
                #tabuleiro.delete(imgWumpus)
            else:
                textoJogo.insert(END, "Você errou!\n")
        elif direcao == 1:
            if (colunaWumpus == colunaJogador) and (wumpus[0][0] < casaJogador):
                textoJogo.insert(END, "Você matou o wumpus!\n")
                - tem_wumpus(casaJogador)
                wumpusVivo = False
                #tabuleiro.delete(imgWumpus)
            else:
                textoJogo.insert(END, "Você errou!\n")
        elif direcao == 2:
            if (linhaWumpus == linhaJogador) and (wumpus[0][0] > casaJogador):
                textoJogo.insert(END, "Você matou o wumpus!\n")
                - tem_wumpus(casaJogador)
                wumpusVivo = False
                #tabuleiro.delete(imgWumpus)
            else:
                textoJogo.insert(END, "Você errou!\n")
        else:
            if (colunaWumpus == colunaJogador) and (wumpus[0][0] > casaJogador):
                textoJogo.insert(END, "Você matou o wumpus!\n")
                - tem_wumpus(casaJogador)
                wumpusVivo = False
                #tabuleiro.delete(imgWumpus)
            else:
                textoJogo.insert(END, "Você errou!\n")
        tiros = tiros - 1
    else:
        textoJogo.insert(END, "Suas balas acabaram!\n")


def bangCima(self):
    textoJogo.insert(END, "Atirou para cima! ")
    casaJogador = getRetangulo(self, coordsCacador[0], coordsCacador[1])
    atirarFlecha(self, casaJogador, 1)


def bangBaixo(self):
    textoJogo.insert(END, "Atirou para baixo! ")
    casaJogador = getRetangulo(self, coordsCacador[0], coordsCacador[1])
    atirarFlecha(self, casaJogador, 3)


def bangEsquerda(self):
    textoJogo.insert(END, "Atirou para a esquerda! ")
    casaJogador = getRetangulo(self, coordsCacador[0], coordsCacador[1])
    atirarFlecha(self, casaJogador, 0)


def bangDireita(self):
    textoJogo.insert(END, "Atirou para a direita! ")
    casaJogador = getRetangulo(self, coordsCacador[0], coordsCacador[1])
    atirarFlecha(self, casaJogador, 2)

pegouOuro = False
def pegaOuro(self):
    global pegouOuro
    if pegouOuro is False:
        ouro = pyDatalog.ask('tem_ouro(X)').answers
        casaJogador = getRetangulo(self, coordsCacador[0], coordsCacador[1])
        if ouro[0][0] == casaJogador:
            textoJogo.insert(END, "Você pegou o ouro!\n")
            print("PEGOU OURO")
            - tem_ouro(casaJogador)
            pegouOuro = True


while (len(buracoRetangulo) < 3):
    num_random = randint(1, 16)
    if ((num_random != 13 and num_random != 14 and num_random != 9) and num_random not in buracoRetangulo):
        buracoRetangulo.append(num_random)
        + tem_poco(num_random)

while (True):
    num_random = randint(1, 16)
    if ((num_random != 13 and num_random != 14 and num_random != 9) and num_random not in buracoRetangulo):
        WumpusRetangulo = num_random
        + tem_wumpus(WumpusRetangulo)
        break

while (True):
    num_random = randint(1, 16)
    if (num_random != 13 and num_random != 14 and num_random != 9) and num_random not in buracoRetangulo and num_random != WumpusRetangulo:
        tesouroWumpus = num_random
        + tem_ouro(num_random)
        break

coordsBuraco1 = tabuleiro.coords(buracoRetangulo[0])
coordsBuraco2 = tabuleiro.coords(buracoRetangulo[1])
coordsBuraco3 = tabuleiro.coords(buracoRetangulo[2])
coordsWumpus = tabuleiro.coords(WumpusRetangulo)
coordsTesouro = tabuleiro.coords(tesouroWumpus)

def desenhaObstaculos():
    global wumpusVivo, coordsCacador
    tabuleiro.create_oval(coordsBuraco1[0], coordsBuraco1[1], coordsBuraco1[2], coordsBuraco1[3], fill="black")
    tabuleiro.create_text(coordsBuraco1[0] + 50, coordsBuraco1[1] + 50, text="BURACO", fill="white")
    tabuleiro.create_oval(coordsBuraco2[0], coordsBuraco2[1], coordsBuraco2[2], coordsBuraco2[3], fill="black")
    tabuleiro.create_text(coordsBuraco2[0] + 50, coordsBuraco2[1] + 50, text="BURACO", fill="white")
    tabuleiro.create_oval(coordsBuraco3[0], coordsBuraco3[1], coordsBuraco3[2], coordsBuraco3[3], fill="black")
    tabuleiro.create_text(coordsBuraco3[0] + 50, coordsBuraco3[1] + 50, text="BURACO", fill="white")
    if wumpusVivo == True:
        tabuleiro.create_image(coordsWumpus[0] + 50, coordsWumpus[1] + 50, image=fotoWumpus)
        tabuleiro.create_image(coordsTesouro[0] + 50, coordsTesouro[1] + 50, image=fotoTesouro)

tabuleiro.bind('<Left>', paraEsquerda)
tabuleiro.bind('<Right>', paraDireita)
tabuleiro.bind('<Up>', paraCima)
tabuleiro.bind('<Down>', paraBaixo)
tabuleiro.bind('<Control-Key-Up>', bangCima)
tabuleiro.bind('<Control-Key-Down>', bangBaixo)
tabuleiro.bind('<Control-Key-Left>', bangEsquerda)
tabuleiro.bind('<Control-Key-Right>', bangDireita)
tabuleiro.focus_set()

tabuleiro.bind('<Button-1>', pegaOuro)
tabuleiro.focus_set()

def Instrucoes():
    janelaInst = Tk()
    janelaInst.geometry("500x400+350+300")
    textoInst = Text(janelaInst, height=20, width=20)
    textoInst.pack(fill=BOTH, expand=YES)
    janelaInst.wm_title("Manual de Instruções")
    textoInst.insert(END, "-Este é o jogo Wumpus, onde o objetivo do jogador é guiar o caçador \n até o tesouro escondido no tabuleiro e retornar o caçador para a sua   posição inicial após a obtenção do tesouro.\n\n")
    textoInst.insert(END, "-Porém, o jogador deve tomar cuidado com o monstro Wumpus e os buracos  que estão escondidos no tabuleiro.Caso o caçador seja movimentado \n para onde estão estes obstáculos, o jogo irá acabar.\n\n")
    textoInst.insert(END, "-Para identificar a aproximação do Wumpus ou dos buracos, a janela \n Game info ao lado do tabuleiro irá informar 'Brisa' quando o jogador   estiver próximo de um buraco ou 'Fedor' quando estiver próximo de um   Wumpus.Quando o caçador estiver na mesma casa que o Tesouro, irá\n aparecer 'Brilho'.\n\n")
    textoInst.insert(END, "-Para movimentar o caçador(neste caso, um pirata), utilize as setas\n direcionais do seu teclado.É possível movimentar o pirata para cima,   para baixo, para esquerda e para a direita!\n\n")
    textoInst.insert(END, "-O pirata tem apenas uma bala em sua arma, logo é capaz de atirar\n apenas uma vez. Para disparar um tiro, o jogador deve segurar Ctrl e   apertar a seta direcional respectiva a direção que ele queira atirar.  O jogador pode atigir o Wumpus se atirar na direção certa ou errar se  atirar em outro.\n\n")
    textoInst.insert(END, "-Para pegar o tesouro, o jogador deve colocar o cursor do mouse sobre   o tabuleiro e pressionar o botão esquerdo do mesmo.Uma mensagem no\n Game Info irá informar se você realmente o pegou!")
    textoInst.config(state=DISABLED)

botaoInst = Button(mainframe, text="Ajuda", command=Instrucoes)
botaoInst.place(x=725, y=20)

def movimentosPossiveis(casaJogador):
    if casaJogador == 1:
        return 2, 5
    elif casaJogador == 2:
        return 1, 3, 6
    elif casaJogador == 3:
        return 2, 4, 7
    elif casaJogador == 4:
        return 3, 8
    elif casaJogador == 5:
        return 1, 6, 9
    elif casaJogador == 6:
        return 2, 5, 7, 10
    elif casaJogador == 7:
        return 3, 6, 8, 11
    elif casaJogador == 8:
        return 4, 7, 12
    elif casaJogador == 9:
        return 5, 10, 13
    elif casaJogador == 10:
        return 6, 9, 11, 14
    elif casaJogador == 11:
        return 7, 10, 12, 15
    elif casaJogador == 12:
        return 8, 11, 16
    elif casaJogador == 13:
        return 9, 14
    elif casaJogador == 14:
        return 10, 13, 15
    elif casaJogador == 15:
        return 11, 14, 16
    else:
        return 12, 15

listaAux = []
listaWumpus = []
listaWumpusCtz = []
listaFedor = []
listaAux = pyDatalog.ask('tem_fedor(X)').answers
for i in listaAux:
    listaFedor.append(i[0])
listaPoco = []
listaPocoCtz = []
listaBrisa = []
listaAux = pyDatalog.ask('tem_brisa(X)').answers
for i in listaAux:
    listaBrisa.append(i[0])
listaVisitados = []
casaAgente = 13

def IA2 (self):
    global listaWumpus, listaWumpusCtz, listaFedor, listaPoco, listaPocoCtz, listaBrisa, listaVisitados, wumpusVivo, pegouOuro, casaAgente, coordsCacador
    atirei = False
    casaBrilho = pyDatalog.ask('tem_ouro(X)').answers[0][0]
    casaAnterior = 13

    casaAgente = getRetangulo(self, coordsCacador[0], coordsCacador[1])
    listaMovPossiveis = movimentosPossiveis(casaAgente)
    num = random.randint(0, 1)
    if listaMovPossiveis[num] == (casaAgente - 1):
        paraEsquerda(self)
    elif listaMovPossiveis[num] == (casaAgente - 4):
        paraCima(self)
    elif listaMovPossiveis[num] == (casaAgente + 1):
        paraDireita(self)
    elif listaMovPossiveis[num] == (casaAgente + 4):
        paraBaixo(self)
    listaVisitados.append(13)

    while True:
        listaAcao = []
        listaMov = []
        listaMovPossiveis = movimentosPossiveis(casaAgente)
        if casaAgente == casaBrilho:
            pegaOuro(self)
        if (casaAgente in listaFedor) and (len(listaWumpusCtz) == 0):
            for casa in listaMovPossiveis:
                if casa not in listaVisitados:
                    if casa not in listaWumpus:
                        listaWumpus.append(casa)
                    elif casa not in listaWumpusCtz:
                        listaWumpusCtz.append(casa)
            listaAcao.append(casaAnterior)
        elif (casaAgente in listaFedor) and (len(listaWumpusCtz) > 0) and (atirei is False) and (wumpusVivo is True):
            linhaWumpus, colunaWumpus = getLinhaColuna(self, listaWumpusCtz[0])
            linhaJogador, colunaJogador = getLinhaColuna(self, casaAgente)
            if linhaWumpus == linhaJogador:
                if casaAgente > listaWumpusCtz[0]:
                    bangEsquerda(self)
                    atirei = True
                    print("TIRO")
                else:
                    bangDireita(self)
                    atirei = True
                    print("TIRO")
            elif colunaWumpus == colunaJogador:
                if casaAgente > listaWumpusCtz[0]:
                    bangCima(self)
                    atirei = True
                    print("TIRO")
                else:
                    bangBaixo(self)
                    atirei = True
                    print("TIRO")
        if (casaAgente in listaBrisa) and (len(listaBrisa) < 3):
            for casa in listaMovPossiveis:
                if casa not in listaVisitados:
                    if casa not in listaPoco:
                        listaPoco.append(casa)
                    elif casa not in listaPocoCtz:
                        listaPocoCtz.append(casa)
            listaAcao.append(casaAnterior)
        if pegouOuro is True:
            acao = listaVisitados[len(listaVisitados) - 1]
            listaVisitados.remove(acao)
            if acao == (casaAgente - 1):
                paraEsquerda(self)
            elif acao == (casaAgente - 4):
                paraCima(self)
            elif acao == (casaAgente + 1):
                paraDireita(self)
            elif acao == (casaAgente + 4):
                paraBaixo(self)
        else:
            for mov in listaMovPossiveis:
                if wumpusVivo is True:
                    if (len(listaWumpusCtz) > 0) and (len(listaPocoCtz) >= 3):
                        if (mov not in listaWumpusCtz) and (mov not in listaPocoCtz):
                            listaMov.append(mov)
                    elif (len(listaWumpusCtz) > 0) and (len(listaPocoCtz) < 3):
                        if (mov not in listaWumpusCtz) and (mov not in listaPoco):
                            listaMov.append(mov)
                    elif (len(listaWumpusCtz) == 0) and (len(listaPocoCtz) >= 3):
                        if (mov not in listaWumpus) and (mov not in listaPocoCtz):
                            listaMov.append(mov)
                    else:
                        if (mov not in listaWumpus) and (mov not in listaPoco):
                            listaMov.append(mov)
                    if len(listaMov) == 0:
                        listaMov.append(listaMovPossiveis[random.randint(0,len(listaMovPossiveis)-1)])
                else:
                    if len(listaPocoCtz) >= 3:
                        if mov not in listaPocoCtz:
                            listaMov.append(mov)
                    elif len(listaPocoCtz) < 3:
                        if mov not in listaPoco:
                            listaMov.append(mov)
                    elif len(listaPocoCtz) >= 3:
                        if mov not in listaPocoCtz:
                            listaMov.append(mov)
                    else:
                        if mov not in listaPoco:
                            listaMov.append(mov)
                    if len(listaMov) == 0:
                        listaMov.append(listaMovPossiveis[random.randint(0,len(listaMovPossiveis)-1)])
            if len(listaAcao) == 0:
                for mov in listaMov:
                    if mov not in listaVisitados:
                        listaAcao.append(mov)
                if len(listaAcao) > 0:
                    random.shuffle(listaAcao)
                    casaAnterior = listaAcao[0]
                    if listaAcao[0] == (casaAgente - 1):
                        paraEsquerda(self)
                    elif listaAcao[0] == (casaAgente - 4):
                        paraCima(self)
                    elif listaAcao[0] == (casaAgente + 1):
                        paraDireita(self)
                    elif listaAcao[0] == (casaAgente + 4):
                        paraBaixo(self)
                else:
                    casaAnterior = listaMov[0]
                    random.shuffle(listaMov)
                    if listaMov[0] == (casaAgente - 1):
                        paraEsquerda(self)
                    elif listaMov[0] == (casaAgente - 4):
                        paraCima(self)
                    elif listaMov[0] == (casaAgente + 1):
                        paraDireita(self)
                    elif listaMov[0] == (casaAgente + 4):
                        paraBaixo(self)
            else:
                casaAnterior = listaAcao[0]
                if listaAcao[0] == (casaAgente - 1):
                    paraEsquerda(self)
                elif listaAcao[0] == (casaAgente - 4):
                    paraCima(self)
                elif listaAcao[0] == (casaAgente + 1):
                    paraDireita(self)
                elif listaAcao[0] == (casaAgente + 4):
                    paraBaixo(self)
        casaAgente = getRetangulo(self, coordsCacador[0], coordsCacador[1])
        if fimDeJogo(casaAgente):
            break

def IA(self):
    global listaWumpus, listaFedor, listaPoco, listaPocoCtz, listaBrisa, listaVisitados, wumpusVivo, pegouOuro, casaAgente, coordsCacador
    casaBrilho = pyDatalog.ask('tem_ouro(X)').answers
    while not fimDeJogo(casaAgente):
        casaAgente = getRetangulo(self, coordsCacador[0], coordsCacador[1])
        listaAux = []
        listaVisitados.append(casaAgente)
        if casaBrilho[0][0] == casaAgente:
            pegaOuro(self)
        listaMovPossiveis = movimentosPossiveis(casaAgente)
        if pegouOuro == 0:
            if (wumpusVivo is True) and (len(listaWumpus) > 0):
                if casaAgente in listaFedor:
                    for mov in listaMovPossiveis:
                        if (mov not in listaVisitados) and (len(listaWumpus) > 0):
                            if mov in listaWumpus:
                                listaWumpus.clear()
                                linhaWumpus, colunaWumpus = getLinhaColuna(self, mov)
                                linhaJogador, colunaJogador = getLinhaColuna(self, casaAgente)
                                if linhaJogador == linhaWumpus:
                                    if casaAgente < mov:
                                        bangDireita(self)
                                    else:
                                        bangEsquerda(self)
                                elif colunaJogador == colunaWumpus:
                                    if casaAgente < mov:
                                        bangBaixo(self)
                                    else:
                                        bangCima(self)
                            else:
                                listaWumpus.append(mov)
            if casaAgente in listaBrisa:
                for mov in listaMovPossiveis:
                    if mov not in listaVisitados:
                        if mov in listaPoco:
                            listaPocoCtz.append(mov)
                        else:
                            listaPoco.append(mov)
            for casa in listaMovPossiveis:
                if (casa not in listaWumpus) and (casa not in listaPoco) and (casa not in listaPocoCtz) and (casa not in listaVisitados):
                    listaAux.append((casa, 10))
                elif (casa not in listaWumpus) and (casa not in listaPoco) and (casa not in listaPocoCtz):
                    listaAux.append((casa, 7))
                elif (casa not in listaWumpus) and (casa not in listaPoco):
                    listaAux.append((casa, 5))
                else:
                    listaAux.append((casa, 3))
            listaAux.sort(key=itemgetter(1), reverse=True)
            if listaAux[0][1] is not 10:
                num = random.randint(0, 1)
                if num == 1:
                    random.shuffle(listaAux)
            if listaAux[0][0] == (casaAgente + 1):
                paraDireita(self)
            elif listaAux[0][0] == (casaAgente + 4):
                paraBaixo(self)
            elif listaAux[0][0] == (casaAgente - 1):
                paraEsquerda(self)
            else:
                paraCima(self)
        else:
            movimento = listaVisitados[len(listaVisitados)-1]
            listaVisitados.remove(movimento)
            if movimento == (casaAgente + 1):
                paraDireita(self)
            elif movimento == (casaAgente + 4):
                paraBaixo(self)
            elif movimento == (casaAgente - 1):
                paraEsquerda(self)
            else:
                paraCima(self)

IA2(mainframe)

mainloop()
