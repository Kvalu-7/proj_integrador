import tkinter as tk
from tkinter import ttk
import random # Usado para gerar dados de exemplo

class TelaConsultaChamada(ttk.Frame):
    """
    Tela para consultar a lista de presença de uma turma específica.
    Organiza os widgets de seleção e a tabela de exibição dos dados.
    """
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        # --- Configuração da Janela Principal ---
        self.container.title("Consulta de Chamada por Turma")
        self.container.geometry("900x600")
        self.container.minsize(700, 500)

        # --- Configuração de Estilos ---
        self.style = ttk.Style(self.container)
        self.style.theme_use("clam")

        # Define cores e fontes para os elementos
        BG_COLOR = "#f0f8ff" # AliceBlue - um azul bem claro
        self.style.configure("TFrame", background=BG_COLOR)
        self.style.configure("TLabel", background=BG_COLOR, font=("Arial", 12))
        self.style.configure("Title.TLabel", font=("Arial", 18, "bold"))
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
        self.style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        self.style.configure("Treeview", font=("Arial", 11), rowheight=25) # Aumenta a altura da linha

        # --- Layout Responsivo ---
        # Configura o grid da janela para que nosso frame principal se expanda
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Coloca este frame (self) na janela principal (container)
        self.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.configure(style="TFrame")

        # Chama o método que cria e posiciona todos os widgets
        self._criar_widgets()
        # Carrega dados iniciais (opcional)
        self._carregar_dados_iniciais()

    def _criar_widgets(self):
        """
        Cria e organiza todos os widgets na tela usando o sistema de grid.
        """
        # --- Configuração do Grid Interno ---
        # A coluna 0 terá todo o peso, fazendo com que a tabela se expanda.
        self.grid_columnconfigure(0, weight=1)
        # A linha 3 terá peso para empurrar a mensagem de status para baixo.
        self.grid_rowconfigure(3, weight=1)

        # --- Frame para os Controles (Seleção de Turma) ---
        # Agrupar os controles em um frame próprio ajuda na organização.
        frame_controles = ttk.Frame(self, style="TFrame")
        frame_controles.grid(row=1, column=0, pady=(0, 20), sticky="ew")
        frame_controles.grid_columnconfigure(1, weight=1) # Faz o combobox se esticar

        # --- Título ---
        label_titulo = ttk.Label(self, text="Consulta de Chamada", style="Title.TLabel")
        label_titulo.grid(row=0, column=0, pady=(10, 20))

        # --- Controles de Seleção ---
        label_turma = ttk.Label(frame_controles, text="Selecione a Turma:")
        label_turma.grid(row=0, column=0, padx=(0, 10))

        self.combo_turmas = ttk.Combobox(frame_controles, state="readonly")
        self.combo_turmas.grid(row=0, column=1, sticky="ew")

        btn_buscar = ttk.Button(frame_controles, text="Buscar", command=self.buscar_chamada)
        btn_buscar.grid(row=0, column=2, padx=(10, 0))

        # --- Tabela (Treeview) para exibir os dados ---
        self.tree = ttk.Treeview(self, columns=("matricula", "nome", "presenca"), show="headings")
        self.tree.heading("matricula", text="Matrícula")
        self.tree.heading("nome", text="Nome do Aluno")
        self.tree.heading("presenca", text="Presença")

        # Define a largura das colunas
        self.tree.column("matricula", width=150, anchor="center")
        self.tree.column("nome", width=400)
        self.tree.column("presenca", width=100, anchor="center")

        self.tree.grid(row=2, column=0, sticky="nsew") # Estica a tabela em todas as direções

        # Adiciona uma barra de rolagem à tabela
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=2, column=1, sticky="ns")

        # --- Mensagem de Status ---
        self.label_mensagem = ttk.Label(self, text="Selecione uma turma e clique em 'Buscar'.", anchor="center")
        self.label_mensagem.grid(row=4, column=0, columnspan=2, pady=(10, 0), sticky="ew")

    def _carregar_dados_iniciais(self):
        """
        Carrega dados iniciais no combobox de turmas.
        No mundo real, isso viria de um banco de dados.
        """
        # Dados de exemplo
        turmas = ["Técnico em Informática - 2024", "Logística - 2023", "Administração - 2024"]
        self.combo_turmas['values'] = turmas
        if turmas:
            self.combo_turmas.current(0) # Seleciona o primeiro item por padrão

    def buscar_chamada(self):
        """
        Função chamada pelo botão 'Buscar'.
        Limpa a tabela e carrega os dados da turma selecionada.
        """
        # Limpa a tabela antes de inserir novos dados
        for item in self.tree.get_children():
            self.tree.delete(item)

        turma_selecionada = self.combo_turmas.get()
        if not turma_selecionada:
            self.label_mensagem.config(text="Erro: Nenhuma turma selecionada.", foreground="red")
            return

        self.label_mensagem.config(text=f"Exibindo chamada para: {turma_selecionada}", foreground="black")

        # --- Simulação de busca de dados ---
        # No mundo real, aqui você faria uma consulta ao banco de dados
        # usando a 'turma_selecionada' como parâmetro.
        dados_exemplo = self._gerar_dados_falsos()

        # Adiciona tags para colorir as linhas
        self.tree.tag_configure('presente', background='#dff0d8') # Verde claro
        self.tree.tag_configure('ausente', background='#f2dede')  # Vermelho claro

        # Insere os dados na tabela
        for aluno in dados_exemplo:
            # Define a tag com base na presença para colorir a linha
            tag = 'presente' if aluno[2] == "Presente" else 'ausente'
            self.tree.insert("", "end", values=aluno, tags=(tag,))

    def _gerar_dados_falsos(self):
        """
        Gera uma lista de alunos para fins de demonstração.
        Substitua isso pela sua lógica de banco de dados.
        """
        nomes = ["Ana Silva", "Bruno Costa", "Carla Dias", "Daniel Souza", "Eduarda Lima", "Felipe Alves", "Gabriela Melo", "Heitor Rocha", "Isabela Nunes", "João Pereira"]
        dados = []
        for i, nome in enumerate(random.sample(nomes, random.randint(5, 10))):
            matricula = f"2024{random.randint(1000, 9999)}"
            presenca = random.choice(["Presente", "Ausente"])
            dados.append((matricula, nome, presenca))
        return dados

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaConsultaChamada(root)
    root.mainloop()
