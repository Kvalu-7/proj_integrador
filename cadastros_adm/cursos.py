import tkinter as tk
from tkinter import ttk

class TelaCadastroCurso(ttk.Frame):
    """
    Tela para cadastro de novos cursos.
    Esta classe organiza todos os elementos visuais (widgets) e a lógica da tela.
    """
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        # --- Configuração da Janela Principal ---
        # Define o título e o tamanho inicial da janela.
        self.container.title("Cadastro de Cursos")
        self.container.geometry("800x600") # Tamanho inicial um pouco menor para telas menores
        self.container.minsize(600, 500) # Define um tamanho mínimo para a janela

        # --- Configuração de Estilos ---
        # Usamos ttk.Style para dar uma aparência mais moderna e consistente.
        self.style = ttk.Style(self.container)
        self.style.theme_use("clam") # 'clam', 'alt', 'default', 'classic' são boas opções

        # Estilo para o frame principal
        self.style.configure("TFrame", background="#f0f0f0")
        # Estilo para os labels (rótulos)
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        # Estilo para o título
        self.style.configure("Title.TLabel", font=("Arial", 18, "bold"))
        # Estilo para os botões
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
        # Estilo para os campos de entrada
        self.style.configure("TEntry", font=("Arial", 12), padding=5)

        # --- Layout Responsivo ---
        # Configura o grid da janela principal para que o frame se expanda
        # com o redimensionamento da janela.
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Coloca este frame (self) na janela principal (container)
        self.grid(row=0, column=0, sticky="nsew")
        self.configure(style="TFrame")

        # Chama o método que cria e posiciona todos os widgets
        self._criar_widgets()

    def _criar_widgets(self):
        """
        Cria e organiza todos os widgets (labels, entries, button) na tela.
        O prefixo '_' indica que este é um método para uso interno da classe.
        """
        # --- Configuração do Grid Interno do Frame ---
        # Criamos colunas "invisíveis" nas laterais (0 e 3) para empurrar o conteúdo
        # para o centro. O 'weight=1' faz com que elas ocupem o espaço extra.
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0) # Coluna para os labels
        self.grid_columnconfigure(2, weight=0) # Coluna para os campos de texto
        self.grid_columnconfigure(3, weight=1)

        # --- Título da Página ---
        self.label_titulo = ttk.Label(self, text="Informações do Curso", style="Title.TLabel")
        # 'columnspan=2' faz o título ocupar as duas colunas centrais.
        self.label_titulo.grid(row=0, column=1, columnspan=2, pady=(20, 30), sticky="ew")

        # --- Campos do Formulário ---
        # Lista de campos para criar o formulário de forma mais fácil
        campos = [
            "Nome do curso:", "Código do curso:", "Carga horária:",
            "Data de início:", "Data de fim:", "Tipo do curso:",
            "Modalidade:", "Turno:", "Unidade:"
        ]

        # Loop para criar cada label e entry
        # 'enumerate' nos dá o índice (i) e o valor (texto_label) da lista
        for i, texto_label in enumerate(campos):
            label = ttk.Label(self, text=texto_label)
            # 'sticky="w"' alinha o texto do label à esquerda (West)
            label.grid(row=i + 1, column=1, padx=(0, 10), pady=5, sticky="w")

            entry = ttk.Entry(self, width=40)
            # 'sticky="ew"' faz o campo de texto se esticar horizontalmente (East-West)
            entry.grid(row=i + 1, column=2, pady=5, sticky="ew")

            # Guardamos uma referência ao entry para poder pegar o valor depois
            # Ex: self.entry_nome_do_curso, self.entry_codigo_do_curso, etc.
            # Isso é feito transformando o texto do label em um nome de variável válido.
            nome_variavel = "entry_" + texto_label.lower().replace(" ", "_").replace(":", "")
            setattr(self, nome_variavel, entry)


        # --- Botão de Cadastro ---
        self.botao_cadastrar = ttk.Button(self, text="Cadastrar", command=self.cadastrar_curso)
        self.botao_cadastrar.grid(row=len(campos) + 1, column=1, columnspan=2, pady=(30, 0), sticky="ew")

    def cadastrar_curso(self):
        """
        Função chamada quando o botão 'Cadastrar' é pressionado.
        Aqui você colocaria a lógica para salvar os dados.
        """
        # Exemplo de como pegar os valores dos campos:
        nome_curso = self.entry_nome_do_curso.get()
        codigo_curso = self.entry_código_do_curso.get()

        print("--- Dados do Curso Cadastrado ---")
        print(f"Nome: {nome_curso}")
        print(f"Código: {codigo_curso}")
        # Você pode adicionar os outros campos aqui
        print("---------------------------------")
        # Futuramente, aqui você pode adicionar a lógica para salvar em um banco de dados
        # ou em um arquivo.
    def notificao_de_campo_limpo(self):
        self.mensagem

if __name__ == "__main__":
    # Cria a janela principal da aplicação
    root = tk.Tk()
    # Cria a nossa tela de cadastro dentro da janela principal
    app = TelaCadastroCurso(root)
    # Inicia o loop principal da aplicação, que a mantém aberta e responsiva
    root.mainloop()

