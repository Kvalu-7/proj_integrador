import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TelaCadastroCurso(ttk.Frame):
    """
    Tela para cadastro de novos cursos, com validação de dados e
    feedback para o usuário.
    """
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        # --- Configuração da Janela Principal ---
        self.container.title("Cadastro de Cursos")
        self.container.geometry("800x600")
        self.container.minsize(600, 550)

        # --- Configuração de Estilos ---
        self.style = ttk.Style(self.container)
        self.style.theme_use("clam")

        BG_COLOR = "#f0f0f0"
        SUCCESS_COLOR = "#006400"  # Verde Escuro
        ERROR_COLOR = "#8B0000"   # Vermelho Escuro

        self.style.configure("TFrame", background=BG_COLOR)
        self.style.configure("TLabel", background=BG_COLOR, font=("Arial", 12))
        self.style.configure("Title.TLabel", font=("Arial", 18, "bold"))
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
        self.style.configure("TEntry", font=("Arial", 12), padding=5)
        # Estilos para as mensagens de feedback
        self.style.configure("Success.TLabel", foreground=SUCCESS_COLOR, font=("Arial", 12, "bold"))
        self.style.configure("Error.TLabel", foreground=ERROR_COLOR, font=("Arial", 12, "bold"))


        # --- Layout Responsivo ---
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")
        self.configure(style="TFrame")

        # Dicionário para guardar as referências dos campos de entrada (Entry)
        self.entries = {}