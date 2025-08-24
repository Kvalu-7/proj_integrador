
import tkinter as tk
from tkinter import ttk
# import Pagina_de_Funcoes as Pf



class POINT:
  def __init__(self,janela):
    self.janela=janela
    self.janela.title("POINT")
    self.janela.geometry("450x420")
    self.janela.configure(bg="#E2E2E2")

    self.var_usuario = tk.StringVar()
    self.var_senha = tk.StringVar()
    

    self.style = ttk.Style()
    #self.style.configure(bg="l")
    # self.style.theme_use("")
    self.criar_widgets()


  def criar_widgets(self):

    frame_up = tk.Frame(self.janela, bg="#002CA7",)
    frame_up.pack(fill="x")

    frame_principal = tk.Frame(self.janela,bg="#E2E2E2")
    frame_principal.pack(fill="both", expand=True, padx=20, pady=8)
    #frame_principal.pack_propagate(False)  # Impede que o frame encolha para caber no conteúdo

    frame_donw = tk.Frame(self.janela, bg="#002CA7", height=200)
    frame_donw.pack(fill="x", pady=15)

      # _____________ TITULO_____________
    intro =tk.Label(frame_up, text=("POINT"),fg="#E2E2E2", bg="#002CA7",font=("arial",30,"italic","bold"))
    intro.pack( padx=5, pady=5)
    intro_sub =tk.Label(frame_up, text=("Ponto Digital"),fg="#E2E2E2", bg="#002CA7",font=("arial",30,"italic","bold"))
    intro_sub.pack( padx=10 )
      # _____________ LOGIN_____________
    login =tk.Label(frame_principal, text="LOGIN",font=("arial",16,"bold"))
    login.config( bg="#E2E2E2")
    login.pack( padx=5, pady=5)

    self.entrada_usuario = tk.Entry(frame_principal, textvariable=self.var_usuario, font=("arial", 16), width=50)
    self.entrada_usuario.pack( padx=5, pady=5)
    self.entrada_usuario.focus()

    senha = tk.Label(frame_principal, text="SENHA",font=("arial",16,"bold"))
    senha.config( bg="#E2E2E2")
    senha.pack( padx=5, pady=5)
    
    self.entrada_senha = tk.Entry(frame_principal, textvariable=self.var_senha, show="*", font=("arial", 16), width=50)
    self.entrada_senha.pack( padx=5, pady=5)
    self.entrada_senha.focus()

    botao_login = tk.Button(frame_principal, text="LOGIN", font=("arial",16,"bold") ,width=20,)
    botao_login.pack(padx=2,pady=5)
    
      # _____________ FOOTER_____________        
    footer =tk.Label(frame_donw, text=("@ todos direitos reservados"),fg="white", bg="#002CA7",font=("arial",12,"italic"))
    footer.pack( padx=5)

    footer2 =tk.Label(frame_donw, text=("TEC. INTERNET - SERVENTE D' SOFTWARE"),fg="white", bg="#002CA7",font=("arial",10,"italic"))
    footer2.pack( padx=10)  
    
    def fazer_login():
      pass
      
      


if __name__== "__main__":
    janela = tk.Tk()
    app= POINT(janela)
    janela.mainloop()
    

