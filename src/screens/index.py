from tkinter import filedialog
import time


def save():
    print('------------------------BEM VINDO------------------------')
    print('obs: esse sistema é feito paara pegar uma planilha de onde \ntem notas de filmes de cada integrante ')
    time.sleep(4)
    print("crie o local do arquivo onde será salvo!!!")
    time.sleep(2)
    return filedialog.asksaveasfile(defaultextension='.json').name



