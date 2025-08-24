import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class TelaCadastroProfessor(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        # --- Configuração da Janela Principal ---
        self.container.title("Cadastro de Professores")
        self.container.geometry("1080x720")
        self.container.minsize(700, 600)# Tamanho mínimo para a janela

        # --- Configuração de Estilos ---
        self.style = ttk.Style(self.container)
        self.style.theme_use("clam")
        BG_COLOR = "#e0e8f0"
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

        # Banco de dados
        self._criar_tabela()

        # Criação dos widgets
        self._criar_entradas()

    def _criar_tabela(self): #função para criar o banco de dados
        conn = sqlite3.connect("instituicao.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS professores (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                Matricula TEXT NOT NULL UNIQUE,
                CPF TEXT NOT NULL UNIQUE CHECK(length( cpf)=11 AND cpf GLOB '[0-9]*'),
                Email TEXT CHECK((instr(email, '@'))>1),
                Status TEXT,
                Cursos TEXT
            
            )
        """)
        conn.commit()
        conn.close()

    def _criar_entradas(self):
    #Cria e organiza todas as informações a serem preenchidas na tela
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        titulo = ttk.Label(self, text="CADASTRAR PROFESSORES", style="Title.TLabel")
        titulo.grid(row=0, column=1, columnspan=2, pady=(20, 30))

        label_nome=ttk.Label(self, text="Nome", style='TLabel')
        label_nome.grid(row=1, column=1,sticky='w' )
        self.entry_nome=ttk.Entry(self, width= 100, style='TEntry')
        self.entry_nome.grid(row=1, column=2, sticky='w')

        label_matricula=ttk.Label(self, text="Matrícula", style='TLabel')
        label_matricula.grid(row=2, column=1,sticky='w' )
        self.entry_matricula=ttk.Entry(self, width= 100, style='TEntry')
        self.entry_matricula.grid(row=2, column=2, sticky='w')

        label_cpf = ttk.Label(self, text="CPF", style='TLabel')
        label_cpf.grid(row=3, column=1, sticky='w')
        self.entry_cpf = ttk.Entry(self, width=100, style='TEntry')
        self.entry_cpf.grid(row=3, column=2, sticky='w')

        label_email = ttk.Label(self, text="E-mail", style='TLabel')
        label_email.grid(row=4, column=1, sticky='w')
        self.entry_email = ttk.Entry(self, width=100, style='TEntry')
        self.entry_email.grid(row=4, column=2, sticky='w')

        label_status = ttk.Label(self, text="Status", style='TLabel')
        label_status.grid(row=5, column=1, sticky='w')
        self.combo_status = ttk.Combobox(self, values=['Ativo', 'Inativo'], font=('Arial', 12))
        self.combo_status.grid(row=5, column=2, sticky='w')

        label_cursos = ttk.Label(self, text="Cursos", style='TLabel')
        label_cursos.grid(row=6, column=1, sticky='w')
        self.combo_cursos = ttk.Combobox(self, values=['...'], font=('Arial', 12))
        self.combo_cursos.grid(row=6, column=2, sticky='w')
            #quando a janela do curso estiver pronta descobrir como ligar ele com o 
            #  professor e jogar aqui no combo 
        
        # --- Botões ---
    
        botao_cadastrar = ttk.Button(self, text="Cadastrar", command=self.cadastrar_professor)
        botao_cadastrar.grid(row=8, column=1, columnspan=2, pady=(30, 10), sticky="ew")

        botao_consultar = ttk.Button(self, text="Consultar registros", command=self.consultar_professores)
        botao_consultar.grid(row=9, column=1, columnspan=2, pady=(10, 20), sticky="ew")

    def cadastrar_professor(self):
        """Salva os dados do professor no banco diretamente dos Entry."""
        try:
            con = sqlite3.connect("instituicao.db")
            cur = con.cursor()
            cur.execute("""
                INSERT INTO professores 
                (Nome, Matricula, CPF, Email, Status, Cursos)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                self.entry_nome.get(),
                self.entry_matricula.get(),
                self.entry_cpf.get(),
                self.entry_email.get(),
                self.combo_status.get(),
                self.combo_cursos.get()
                
            ))
            con.commit()
            con.close()

            messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso!")
            self._limpar_campos()

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar os dados:\n{e}")

    def consultar_professores(self):
        """Abre uma nova janela com todos os professores cadastrados e permite deletar."""
        consulta_win = tk.Toplevel(self.container)
        consulta_win.title("Consulta de Professores")
        consulta_win.geometry("900x400")

        colunas = ("ID", "Nome", "Matrícula", "CPF", "Email", "Status", "Cursos")
        tree = ttk.Treeview(consulta_win, columns=colunas, show="headings")

        for col in colunas:
            tree.heading(col, text=col.capitalize())
            tree.column(col, width=100)

        tree.pack(expand=True, fill="both")

        con = sqlite3.connect("instituicao.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM professores")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        con.close()

        # Botão para deletar registro selecionado
        def deletar_selecionado():
            item = tree.selection()
            if not item:
                messagebox.showerror("Erro", "Selecione um professor para deletar!")
                return

            professor_id = tree.item(item)["values"][0]

            con = sqlite3.connect("instituicao.db")
            cursor = con.cursor()
            cursor.execute("DELETE FROM professores WHERE id=?", (professor_id,))
            con.commit()
            con.close()

            tree.delete(item)
            messagebox.showinfo("Sucesso", "Professor deletado com sucesso!")

        botao_deletar = ttk.Button(consulta_win, text="Deletar Selecionado", command=deletar_selecionado)
        botao_deletar.pack(pady=10)

    def _limpar_campos(self): #apos salvar os dados limpar os campos
        self.entry_nome.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.combo_status.set(" ") 
        self.combo_cursos.set(" ")










if __name__ == "__main__":
    root = tk.Tk()
    app = TelaCadastroProfessor(root)
    root.mainloop()
