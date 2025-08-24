import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TelaCadastroProfessor(ttk.Frame):
    """
    Tela para o cadastro de dados de um professor.
    A classe organiza a criação de todos os widgets e a lógica da tela.
    """
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        # --- Configuração da Janela Principal ---
        self.container.title("Cadastro de Professores")
        self.container.geometry("1080x720")
        self.container.minsize(700, 600) # Tamanho mínimo para a janela

        # --- Configuração de Estilos ---
        self.style = ttk.Style(self.container)
        self.style.theme_use("clam")

        BG_COLOR = "#e0e8f0" # Um azul acinzentado claro
        self.style.configure("TFrame", background=BG_COLOR)
        self.style.configure("TLabel", background=BG_COLOR, font=("Arial", 12))
        self.style.configure("Title.TLabel", font=("Arial", 18, "bold"))
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
        self.style.configure("TEntry", font=("Arial", 12), padding=5)

        # --- Layout Responsivo ---
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")
        self.configure(style="TFrame")

        # Chama o método que cria e posiciona todos os widgets
        self._criar_widgets()

    def _criar_widgets(self):
        """
        Cria e organiza todos os widgets (labels, entries, button) na tela.
        """
        # --- Configuração do Grid Interno para Centralização ---
        # Colunas 0 e 3 são espaçadores invisíveis.
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0) # Coluna dos labels
        self.grid_columnconfigure(2, weight=1) # Coluna dos entries (com peso para expandir)
        self.grid_columnconfigure(3, weight=1)

        # --- Título ---
        titulo = ttk.Label(self, text="Cadastro de Pessoal Administrativo", style="Title.TLabel")
        titulo.grid(row=0, column=1, columnspan=2, pady=(20, 30))

        # --- Campos do Formulário ---
        # Criamos uma lista com todos os campos que queremos no formulário.
        # Se amanhã você precisar adicionar um novo campo, basta adicioná-lo a esta lista!
        campos_formulario = [
            "Nome do Professor:", "CPF:", "Telefone:", "email:", "Matrícula:",
            "Curso 1:", "Curso 2:", "Curso 3:", "Curso 4:"
        ]

        # Loop para criar cada label e entry de forma automática
        for i, texto_label in enumerate(campos_formulario):
            # O 'i+1' é para começar a colocar os campos a partir da linha 1 (abaixo do título)
            linha_atual = i + 1

            label = ttk.Label(self, text=texto_label)
            label.grid(row=linha_atual, column=1, padx=(0, 10), pady=5, sticky="w")

            entry = ttk.Entry(self, width=40)
            entry.grid(row=linha_atual, column=2, pady=5, sticky="ew")

            # Guardamos uma referência ao entry para poder pegar o valor depois.
            # Transforma "Nome do Professor:" em "entry_nome_do_professor"
            nome_variavel = "entry_" + texto_label.lower().replace(" ", "_").replace(":", "")
            setattr(self, nome_variavel, entry)

        # --- Botão de Cadastro ---
        # A linha do botão será a próxima linha depois do último campo do loop
        linha_botao = len(campos_formulario) + 1
        botao_cadastrar = ttk.Button(self, text="Cadastrar", command=self.cadastrar_professor)
        botao_cadastrar.grid(row=linha_botao, column=1, columnspan=2, pady=(30, 20), sticky="ew")

    def cadastrar_professor(self):
        """
        Função chamada quando o botão 'Cadastrar' é pressionado.
        Coleta os dados de todos os campos e os imprime.
        """
        print("--- Dados do Professor Cadastrado ---")

        # Exemplo de como pegar os valores dos campos que foram criados dinamicamente:
        nome_prof = self.entry_nome_do_professor.get()
        cpf_prof = self.entry_cpf.get()
        email_prof = self.entry_email.get() # Note que o "E-mail" virou "e_mail"

        print(f"Nome: {nome_prof}")
        print(f"CPF: {cpf_prof}")
        print(f"E-mail: {email_prof}")
        # Você pode adicionar os outros campos aqui...
        print("---------------------------------")
        # Aqui viria a lógica para salvar os dados em um banco de dados.
    
    def cadastrar_professor2(self):
        """
        Coleta os dados dos campos, valida e simula o cadastro.
        """
        # Coleta os dados de todos os campos
        dados_professor = {
            "nome": self.entry_nome_do_professor.get(),
            "cpf": self.entry_cpf.get(),
            "telefone": self.entry_telefone.get(),
            "email": self.entry_email.get(),
            "matricula": self.entry_matricula.get(),
            "curso1": self.entry_curso_1.get(),
            "curso2": self.entry_curso_2.get(),
            "curso3": self.entry_curso_3.get(),
            "curso4": self.entry_curso_4.get()
        }

        # Validação simples: Verifica se o nome e CPF estão preenchidos
        if not dados_professor["nome"] or not dados_professor["cpf"]:
            messagebox.showerror("Erro", "Nome e CPF são obrigatórios!")
            return

        # Simulação de cadastro (aqui você chamaria a função para salvar no banco de dados)
        print("--- Dados do Professor para Salvar ---")
        for campo, valor in dados_professor.items():
            print(f"{campo.replace('_', ' ').title()}: {valor}")
        print("---------------------------------")

        # Feedback ao usuário
        messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso!")
        
    def _mostrar_notificacao(self, mensagem, tipo):
        """
        Exibe uma mensagem para o usuário.
        'tipo' pode ser "Success" ou "Error".
        """
        if tipo == "Success":
            messagebox.showinfo("Sucesso", mensagem)
        elif tipo == "Error":
            messagebox.showerror("Erro", mensagem)
        
    def _limpar_campos(self):
        """
        Limpa o texto de todos os campos de entrada (Entry).
        """
        for campo in ["nome_do_professor", "cpf", "telefone", "email", "matricula",
                      "curso_1", "curso_2", "curso_3", "curso_4"]:
            entry = getattr(self, f"entry_{campo}", None)
            if entry:
                entry.delete(0, tk.END)


if __name__ == "__main__":
    # Cria a janela principal da aplicação
    root = tk.Tk()
    # Cria a nossa tela de cadastro dentro da janela principal
    app = TelaCadastroProfessor(root)
    # Inicia o loop principal da aplicação
    root.mainloop()