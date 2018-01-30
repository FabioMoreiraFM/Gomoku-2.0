# encoding: utf-8
from tkinter import *
from tkinter.messagebox import showinfo 
from jogador import *

class View():
    root = None
    controller = None
    frame_board = None
    frame_info = None
    frame_score = None
    entry_nome = None
    jogador_2 = None
    entry_tamanho_tabuleiro = None
    tamanho_tabuleiro = None
    tipo_partida = False
    jogador_vez = None
    nome_jogador = ""
    guarda_canvas = None
    guarda_coord = None

    def __init__(self, controller):
        self.root = Tk()
        self.root.title('Ultimate Gomoku Bamboozled')

        self.controller = controller

    def create_frame_board(self):
        self.frame_board = Frame(self.root)
        self.tamanho_tabuleiro = int(self.entry_tamanho_tabuleiro.get())
        self.guarda_canvas = {}
        self.guarda_coord = {}
        rows = self.tamanho_tabuleiro
        columns = self.tamanho_tabuleiro
        for row in range(rows):
            for column in range(columns):
                canvas = Canvas(self.frame_board, width=15, height = 15, borderwidth=0, bg='blue')
                canvas.bind("<Button-1>", self.board_click)
                canvas.grid(row=row, column=column, padx=1, pady=1)
                self.guarda_canvas[canvas] = [column, row]
                self.guarda_coord[column,row] = canvas

        for column in range(columns):
            self.frame_board.grid_columnconfigure(column, weight=1)

        self.frame_board.grid(row=0, column=0, padx=10, pady=10)

    def board_click(self, event):
        jogador_atual, erro = self.controller.vez_humano(self.guarda_canvas[event.widget])
        if erro:
            return
        self.trocar_jogador_atual(jogador_atual)
        
        if jogador_atual == Jogador.ADVERSARIO_1:
            event.widget.configure(bg='black')
        else:
            event.widget.configure(bg='white')

        if not(self.tipo_partida):
            self.guarda_coord[self.controller.vez_ia()].configure(bg='white')  

        self.controller.verifica_fim_jogo()
        self.trocar_jogador_atual(jogador_atual)

    def create_frame_info(self):
        self.frame_info = Frame(self.root)
        self.frame_info.grid(row=0, column=1)

        label_info = Label(self.frame_info, text="Custom Match")
        label_info.grid(row=0,column=0, columnspan=4)

        label_nome = Label(self.frame_info, text="Nome do Jogador: ")
        label_nome.grid(row=1, column=0, sticky=W)

        self.entry_nome = Entry(self.frame_info)
        self.entry_nome.grid(row=1, column=1)

        label_tamanho_tabuleiro = Label(self.frame_info, text="Tamanho do tabuleiro: ")
        label_tamanho_tabuleiro.grid(row=2, column=0, sticky=W)

        self.entry_tamanho_tabuleiro = Entry(self.frame_info)
        self.entry_tamanho_tabuleiro.grid(row=2, column=1)

        label_tipo_partida = Label(self.frame_info, text="Tipo de partida: ").grid(row=3, column=0, sticky=W)
        radio_hh = Radiobutton(self.frame_info, text="PvP", variable="Tipo_partida", value=1, command=lambda: self.set_tipo_partida(True)).grid(row=3, column=1, sticky=W)
        radio_hia = Radiobutton(self.frame_info, text="PvE", variable="Tipo_partida", value=2, command=lambda: self.set_tipo_partida(False)).grid(row=3, column=1, sticky=E)

        label_dificuldade = Label(self.frame_info, text="Dificuldade: ").grid(row=4, column=0, sticky=W)
        facil= Radiobutton(self.frame_info, text="Fácil", variable="dificuldade", value=1, command=lambda: self.set_dificuldade(3)).grid(row=4, column=1, sticky=W)
        medio = Radiobutton(self.frame_info, text="Médio", variable="dificuldade", value=2, command=lambda: self.set_dificuldade(4)).grid(row=4, column=1, sticky=E)
        dificil = Radiobutton(self.frame_info, text="Difícil", variable="dificuldade", value=3, command=lambda: self.set_dificuldade(5)).grid(row=4, column=2, sticky=E)

        btn_inicio_jogo = Button(self.frame_info, text="Iniciar partida", command=self.iniciar_jogo)
        btn_inicio_jogo.grid(row=5, column=0, columnspan=4)

    def create_frame_score(self):
        self.nome_jogador = self.entry_nome.get()
        self.frame_info.destroy()

        self.frame_score = Frame(self.root)
        self.frame_score.grid(row=0, column=1)

        label_title_score = Label(self.frame_score, text="Informações da partida").grid(row=0, column=0, columnspan=4)
        tipo_partida = "PvP" if self.tipo_partida else "PvE"
        label_title_partida = Label(self.frame_score, text="Tipo de partida: " + tipo_partida).grid(row=1, column=0, sticky=W)

        label_nome_jogador = Label(self.frame_score, text="Nome Jogador 1: " + self.nome_jogador).grid(row=2, column=0, sticky=W)

        
        self.jogador_2 = "Cetoconazol" if self.tipo_partida else "Computador"

        label_nome_jogador_2 = Label(self.frame_score, text="Nome Jogador 2: " + self.jogador_2).grid(row=3, column=0, sticky=W)

        self.jogador_vez = StringVar()
        self.jogador_vez.set("Esperando Jogador: " + self.nome_jogador)
        label_vez_do_jogador = Label(self.frame_score, textvariable=self.jogador_vez).grid(row=4, column=0, sticky=W)

    def menu_inicial(self):
        self.create_frame_info()
        self.root.mainloop()

    def iniciar_jogo(self):
        self.create_frame_board()
        self.create_frame_score()
        self.controller.configuracoes_iniciais(self.tipo_partida, self.tamanho_tabuleiro, self.dificuldade)

    def set_tipo_partida(self, opcao):
        self.tipo_partida = opcao

    def trocar_jogador_atual(self, jogador):
        self.jogador_vez.set("Esperando Jogador: {}".format(self.nome_jogador if jogador == Jogador.ADVERSARIO_2 else self.jogador_2))

    def opcao_jogo(self):
        return self.tipo_partida

    def tamanho_tabuleiro(self):
        return self.tamanho_tabuleiro

    def mensagem_fim_de_jogo(self, jogador_vencedor):
        showinfo("Game Over", "Parabéns {}, você ganhou!".format(self.nome_jogador if jogador_vencedor == Jogador.ADVERSARIO_1 else self.jogador_2))
        self.root.destroy()

    def msg_erro_inserir_peca(self):
        showinfo("Jogada inválida", "Não é possível adicionar uma peça nessa posição!")
    
    def set_dificuldade(self, nivel_dificuldade):
        self.dificuldade = nivel_dificuldade