from tkinter import ttk
import tkinter as tk
from tkinter import Tk

import PABLO_FRONT.Erick.LOGIN101 as logi


class Main_point:
    def __init__(self, root):
        self.root = root
        # Aqui você pode inicializar a tela de login ou outras funcionalidades
        self.login_screen = logi.POINT(self.root)  # Exemplo de inicialização de uma tela de login

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Registro de Ponto")
    root.geometry("800x600")
    root.configure(bg='#FFFFFF')

    # Inicia o sistema com a tela de login
    app = Main_point(root)

    # Inicia o loop principal da interface gráfica
    root.mainloop()