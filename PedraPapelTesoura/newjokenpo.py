from tkinter import *
import random
import time

# Variáveis globais para contagem de vitórias
vitorias_jogador = 0
vitorias_computador = 0

def escolher_jogada_computador():
    jogadas = ["Pedra", "Papel", "Tesoura"]
    return random.choice(jogadas)

def verificar_resultado(jogada_jogador, jogada_computador):
    global vitorias_jogador, vitorias_computador
    
    if jogada_jogador == jogada_computador:
        return "Empate", jogada_computador
    elif (
        (jogada_jogador == "Pedra" and jogada_computador == "Tesoura")
        or (jogada_jogador == "Papel" and jogada_computador == "Pedra")
        or (jogada_jogador == "Tesoura" and jogada_computador == "Papel")
    ):
        vitorias_jogador += 1
        return "Você ganhou", jogada_computador
    else:
        vitorias_computador += 1
        return "Você perdeu", jogada_computador

def tela_abertura():
    abertura = Toplevel()
    abertura.title("Abertura")
    abertura.geometry(f"{jan.winfo_width()}x{jan.winfo_height()}+200+100")
    
    label_abertura = Label(abertura, text="", font=("ComicSans", 24))
    label_abertura.pack(pady=10)
    
    label_abertura.update()
    time.sleep(0.5)
    label_abertura.config(text="Jo",font=("ComicSans", 120))
    label_abertura.update()
    
    time.sleep(0.5)
    label_abertura.config(text="Jo Ken",font=("ComicSans", 120))
    label_abertura.update()
    
    time.sleep(0.5)
    label_abertura.config(text="Jo Ken Po",font=("ComicSans", 120))
    label_abertura.update()
    
    time.sleep(1)
    
    abertura.destroy()
    jogar_jokenpo(escolher_jogada_computador())

def jogar_jokenpo(escolha_jogador):
    global vitorias_jogador, vitorias_computador
    
    # Cria a tela de resultado na mesma posição das outras
    resultado_janela = Toplevel()
    resultado_janela.title("Resultado")
    resultado_janela.geometry(f"{jan.winfo_width()}x{jan.winfo_height()}+200+100")
    
    jogada_computador = escolher_jogada_computador()
    resultado, jogada_comp = verificar_resultado(escolha_jogador, jogada_computador)
    
    imagem_jogador = PhotoImage(file=f"imagens/{escolha_jogador.lower()}.png")
    imagem_computador = PhotoImage(file=f"imagens/{jogada_comp.lower()}.png")
    
    frame = Frame(resultado_janela)
    frame.pack()
    
    label_jogador = Label(frame, image=imagem_jogador)
    label_jogador.image = imagem_jogador
    label_jogador.grid(row=0, column=0)
    
    label_versus = Label(frame, text="Versus", font=("ComicSans", 24))
    label_versus.grid(row=0, column=1)
    
    label_computador = Label(frame, image=imagem_computador)
    label_computador.image = imagem_computador
    label_computador.grid(row=0, column=2)
    
    label_vitorias = Label(resultado_janela, text=f"Vitórias Jogador: {vitorias_jogador}\nVitórias Computador: {vitorias_computador}", font=("ComicSans", 14))
    label_vitorias.pack()
    
    fechar_button = Button(resultado_janela, text="Fechar", command=resultado_janela.destroy)
    fechar_button.pack()

jan = Tk()
   
jan.title('JoKenPo')
jan.geometry("870x400+200+100")

img_pedra = PhotoImage(file="imagens/pedra.png")
img_tesoura = PhotoImage(file="imagens/tesoura.png")
img_papel = PhotoImage(file="imagens/papel.png")

label_um = Label(jan, text='Faça sua escolha!', font=('ComicSans', 35))
label_um.grid(row=0, column=1)

pedra = Button(jan, image=img_pedra, bg='blue', command=lambda: tela_abertura())
pedra.grid(row=1, column=0)

tesoura = Button(jan, image=img_tesoura, bg='red', command=lambda: tela_abertura())
tesoura.grid(row=1, column=1)

papel = Button(jan, image=img_papel, bg='green', command=lambda: tela_abertura())
papel.grid(row=1, column=2)

jan.mainloop()
