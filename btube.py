# Importações ----------------------------------
from tkinter import *
from tkinter import ttk
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog as dlg
from tkinter import messagebox
from pytube.exceptions import RegexMatchError

# Janela principal
janela = Tk()
janela.geometry("560x150")
janela.title("Baixador Btube")
janela.configure(bg='#E4EEF2')
icone = PhotoImage(file ='icone.ico')
janela.iconphoto(False, icone)
janela.resizable(width=False, height=False)
janela.minsize(width=560, height=150)
janela.maxsize(width=560, height=150)


def baixar(link_):
    '''Faz o download do vídeo escolhendo a pasta onde deseja salvar'''
    try:
        pasta = dlg.askdirectory()
        YouTube(link_).streams.get_highest_resolution().download(pasta)
        tk.messagebox.showinfo(title='Download Concluído', message='Download concluído com sucesso!')
    except RegexMatchError:
        tk.messagebox.showerror(title='Falha Download', message='Falha no Download!')


def limpar():
    '''Limpa a entry onde insere o link'''
    entry_link.delete(0,tk.END)


# Label e Entry --------------------------------------------------
label_link = Label(janela, text="Link do vídeo:", font=("Helvetica", 12), bg='#E4EEF2', fg='#035373')
label_link.place(x=20, y=36)

entry_link = Entry(janela, width = 40, font = ('Helvetica', 12))
entry_link.place(x=160, y=40)


# Botões (Baixar e limpar)
botao_baixar = Button(janela, text = 'Baixar', width=12, font=('Helvetica',9), bg='#0588A6', fg='#E4EEF2', command=lambda:baixar(entry_link.get()))
botao_baixar.place(x=160, y=90)

botao_limpar = Button(janela, text = 'Limpar', width=15, font=('Helvetica',9), bg='#0588A6', fg='#E4EEF2', command=limpar)
botao_limpar.place(x=270, y=90)


label_by = Label(janela, text="By Stefano", font=("Helvetica", 8), bg='#E4EEF2', fg='#035373')
label_by.place(x=470, y=120)

janela.mainloop()