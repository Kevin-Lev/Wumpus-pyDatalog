from tkinter import *

class Tabuleiro(Frame):
    def __init__(self, parent, linhas=8, colunas=8, tam=32, cor1="white", cor2="green"):
        #tam é o tamanho de um quadrado em pixels

        self.linhas = linhas
        self.colunas = colunas
        self.size = size
        self.cor1 = cor1
        self.cor2 = cor2
        self.pieces = {}

        largura_canvas = colunas * tam
        altura_canvas = linhas * tam

        Frame.__init__(self, parent)
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0, width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(fill=BOTH, expand = True, padx=2, pady=2)
