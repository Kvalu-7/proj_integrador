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

        self._criar_widgets()

    def _criar_widgets(self):
        """
        Cria e organiza todos os widgets na tela.
        """
        # --- Configuração do Grid Interno ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1) # Damos peso à coluna dos entries para expandir
        self.grid_columnconfigure(3, weight=1)

        # --- Título da Página ---
        label_titulo = ttk.Label(self, text="Informações do Curso", style="Title.TLabel")
        label_titulo.grid(row=0, column=1, columnspan=2, pady=(20, 30))

        # --- Campos do Formulário ---
        campos = [
            "Nome do curso:", "Código do curso:", "Carga horária:",
            "Data de início:", "Data de fim:", "Tipo do curso:",
            "Modalidade:", "Turno:", "Unidade:"
        ]

        for i, texto_label in enumerate(campos):
            linha_atual = i + 1
            label = ttk.Label(self, text=texto_label)
            label.grid(row=linha_atual, column=1, padx=(0, 10), pady=5, sticky="w")

            entry = ttk.Entry(self, width=40)
            entry.grid(row=linha_atual, column=2, pady=5, sticky="ew")

            # Guardamos o entry em um dicionário para fácil acesso depois
            nome_variavel = texto_label.lower().replace(" ", "_").replace(":", "")
            self.entries[nome_variavel] = entry

        # --- Botão de Cadastro ---
        linha_widgets = len(campos) + 1
        botao_cadastrar = ttk.Button(self, text="Cadastrar", command=self.cadastrar_curso)
        botao_cadastrar.grid(row=linha_widgets, column=1, columnspan=2, pady=(30, 10), sticky="ew")

        # --- Label para Notificações ---
        # Este label ficará invisível até que uma mensagem seja definida
        self.label_notificacao = ttk.Label(self, text="", anchor="center")
        self.label_notificacao.grid(row=linha_widgets + 1, column=1, columnspan=2, pady=(5, 0))

    def cadastrar_curso(self):
        """
        Coleta os dados, valida, salva (simulação) e dá feedback ao usuário.
        """
        # 1. Coletar dados de todos os campos
        dados_curso = {}
        for nome, entry in self.entries.items():
            dados_curso[nome] = entry.get()

        # 2. Validar os dados
        # Verificamos se o campo mais importante, o nome, não está vazio.
        if not all (dados_curso.values()) or not dados_curso["nome_do_curso"]:
            self._mostrar_notificacao("Todos os campos são obrigatórios!", "Error")
            return # Para a execução da função aqui se a validação falhar
            

        # 3. Salvar os dados (Simulação)
        # No mundo real, aqui você chamaria a função para salvar no banco de dados.
        print("--- Dados do Curso para Salvar ---")
        for nome, valor in dados_curso.items():
            print(f"{nome.replace('_', ' ').title()}: {valor}")
        print("---------------------------------")

        # 4. Dar feedback de sucesso e limpar os campos
        self._mostrar_notificacao("Curso cadastrado com sucesso!", "Success")
        self._limpar_campos()

    def _mostrar_notificacao(self, mensagem, tipo):
        """
        Exibe uma mensagem para o usuário.
        'tipo' pode ser "Success" ou "Error".
        """
        self.label_notificacao.config(text=mensagem, style=f"{tipo}.TLabel")

    def _limpar_campos(self):
        """
        Limpa o texto de todos os campos de entrada (Entry).
        """
        for entry in self.entries.values():
            entry.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaCadastroCurso(root)
    root.mainloop()