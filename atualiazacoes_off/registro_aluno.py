import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class TelaCadastroAluno(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        # --- Configuração da Janela Principal ---
        self.container.title("Cadastro de Alunos")
        self.container.geometry("800x600")
        self.container.minsize(600, 500) # Define um tamanho mínimo

        # --- Configuração de Estilos ---
        self.style = ttk.Style(self.container)
        self.style.theme_use("clam")
        BG_COLOR = "#f0f0f0" # Um cinza bem claro e neutro
        self.style.configure("TFrame", background=BG_COLOR)
        self.style.configure("TLabel", background=BG_COLOR, font=("Arial", 12))
        self.style.configure("Title.TLabel", font=("Arial", 18, "bold"))
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
        self.style.configure("TEntry", font=("Arial", 12), padding=5)

        # --- Layout Responsivo ---
        # Faz o frame principal se expandir com a janela
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")
        self.configure(style="TFrame")

        # Chama o método que cria e posiciona todos os widgets
        self.criar_banco()
        self.informacoes_alunos()

    def criar_banco(self):
        conn=sqlite3.connect("instituicao.db")
        cursor=conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                Matricula TEXT NOT NULL UNIQUE,
                CPF TEXT NOT NULL UNIQUE CHECK(length(cpf)=11 AND CPF GLOB '[0-9]*'),
                Email TEXT NOT NULL CHECK((instr(email, '@'))>1),
                Curso TEXT
        )
    """)
        conn.commit()
        conn.close()

    def informacoes_alunos(self):
        # --- Configuração do Grid Interno para Centralização ---
        # Colunas 0 e 3 são espaçadores invisíveis que empurram o conteúdo para o centro.
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0) # Coluna dos labels
        self.grid_columnconfigure(2, weight=1) # Coluna dos entries (com peso para expandir)
        self.grid_columnconfigure(3, weight=1)

        # --- Título ---
        titulo = ttk.Label(self, text="CADASTRAR ALUNOS", style="Title.TLabel")
        titulo.grid(row=0, column=1, columnspan=2, pady=(20, 30))

        label_nome=ttk.Label(self, text="Nome", style='TLabel')
        label_nome.grid(row=1, column=1,sticky='w' )
        self.entry_nome=ttk.Entry(self, width= 100, style='TEntry')
        self.entry_nome.grid(row=1, column=2, sticky='w')

        label_matricula=ttk.Label(self, text="Matricula", style='TLabel')
        label_matricula.grid(row=2, column=1,sticky='w' )
        self.entry_matricula=ttk.Entry(self, width= 100, style='TEntry')
        self.entry_matricula.grid(row=2, column=2, sticky='w')

        label_cpf=ttk.Label(self, text="CPF", style='TLabel')
        label_cpf.grid(row=3, column=1,sticky='w' )
        self.entry_cpf=ttk.Entry(self, width= 100, style='TEntry')
        self.entry_cpf.grid(row=3, column=2, sticky='w')

        label_email=ttk.Label(self, text="Email", style='TLabel')
        label_email.grid(row=4, column=1,sticky='w' )
        self.entry_email=ttk.Entry(self, width= 100, style='TEntry')
        self.entry_email.grid(row=4, column=2, sticky='w')

        label_curso=ttk.Label(self, text="Curso", style='TLabel')
        label_curso.grid(row=5, column=1,sticky='w' )
        self.combo_curso=ttk.Combobox(self,values=[' '], font=("Arial", 12))
        self.combo_curso.grid(row=5, column=2, sticky='w')

        #========Botões==========

        botao_cadastrar = ttk.Button(self, text="Cadastrar", command=self.cadastrar_alunos)
        botao_cadastrar.grid(row=8, column=1, columnspan=2, pady=(30, 10), sticky="ew")

        botao_consultar = ttk.Button(self, text="Consultar registros", command=self.consultar_dados_alunos)
        botao_consultar.grid(row=9, column=1, columnspan=2, pady=(10, 20), sticky="ew")

    def cadastrar_alunos(self):
        try:
            con= sqlite3.connect("instituicao.db")
            cur=con.cursor()
            cur.execute("""
                INSERT INTO alunos
                (Nome, Matricula, CPF, Email, Curso)
                VALUES(?, ?, ?, ?, ?)
            """,(
                self.entry_nome.get(),
                self.entry_matricula.get(),
                self.entry_cpf.get(),
                self.entry_email.get(),
                self.combo_curso.get()
            
            ))
            con.commit()
            con.close()

            messagebox.showinfo("Ok", "Aluno cadastrado com sucesso")
            self._limpar_campos()
        
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados{e}")

    def consultar_dados_alunos(self):
        area_consulta = tk.Toplevel(self.container)
        area_consulta.title("Dados dos alunos")
        area_consulta.geometry("900x400")

        colunas = ("ID", "Nome", "Matrícula", "CPF", "Email", "Curso")
        tree = ttk.Treeview(area_consulta, columns=colunas, show="headings")

        for col in colunas:
            tree.heading(col, text=col.capitalize())
            tree.column(col, width=100)

        tree.pack(expand=True, fill="both")

        con = sqlite3.connect("instituicao.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM alunos")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        con.close()

        def deletar_selecionado():
                item = tree.selection()
                if not item:
                    messagebox.showerror("Erro", "Selecione um aluno para deletar!")
                    return

                professor_id = tree.item(item)["values"][0]

                con = sqlite3.connect("instituicao.db")
                cursor = con.cursor()
                cursor.execute("DELETE FROM alunos WHERE id=?", (professor_id,))
                con.commit()
                con.close()

                tree.delete(item)
                messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")
        #============botão para deletar um registro=============
        botao_deletar = ttk.Button(area_consulta, text="Deletar Selecionado", command=deletar_selecionado)
        botao_deletar.pack(pady=10)

    def _limpar_campos(self): #apos salvar os dados limpar os campos
        self.entry_nome.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.combo_curso.set(" ")




if __name__ == "__main__":
    root = tk.Tk()
    app = TelaCadastroAluno(root)
    root.mainloop()
