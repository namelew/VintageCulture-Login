# Importar as bibliotecas

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import DataBaser

# ==================Criando janelas  =======================

jan= Tk()
jan.title("System Login - Rafis")
jan.geometry("600x300")
jan.configure(background="BLACK")
jan.resizable(width=False , height=False)
jan.attributes("-alpha",0.9) # transparência

#=======================Acrescentando Imagem =============

logo = PhotoImage(file="vintage.png")

#======================= Widget============================
Leftframe = Frame(jan, width=200, height=300 ,bg="WHITE", relief="raise")
Leftframe.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300 ,bg="WHITE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(Leftframe, image=logo, bg='WHITE')
LogoLabel.place(x=-25,y=40)

UserLabel = Label(RightFrame,text="USERNAME:", font=("Central Gothic",15),bg="WHITE", fg='black')
UserLabel.place(x=10, y=125)

UserEntry = ttk.Entry(RightFrame,width=30)
UserEntry.place(x=135, y=125)

PassLabel = Label(RightFrame,text="PASSWORD:", font=("Central Gothic",15),bg="WHITE", fg='black')
PassLabel.place(x=8, y=150)

PassEntry = ttk.Entry(RightFrame,width=30, show="*" )
PassEntry.place(x=135, y=150)

#======================= Botões =======================
def login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    
    DataBaser.cursor.execute(''' 
                             SELECT * FROM Users 
                             WHERE(User = ? and Password = ?)
                             ''', (User,Pass))
    print("Selecionou")
    verifyLogin = DataBaser.cursor.fetchone()
    try:
        if(User in verifyLogin and Pass in verifyLogin):
            messagebox.showinfo(title="Login info", message="Acesso Confirmado")
            
    except:
         messagebox.showinfo(title="Login info", message="Acesso negado!")
        
        
    
LoginButton = ttk.Button(RightFrame, text="login", width=20, command=login)
LoginButton.place(x=135, y=200)


def Register():
    # Tirando Widgets de login
    LoginButton.place(x=50000)
    RegistreButton.place(x=50000)
    
    # Inserindo Cadastro novo
    NomeLabel= Label(RightFrame,text="NAME:", font=("Century Gothic",15), bg="WHITE", fg='black')
    NomeLabel.place(x=5,y=5)
    
    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=74, y=7)
    
    EmailLabel= Label(RightFrame,text="E-MAIL:", font=("Century Gothic",15), bg="WHITE", fg='black')
    EmailLabel.place(x=10,y=35)
    
    EmailEntry = Entry(RightFrame, width=37)
    EmailEntry.place(x=87, y=38)
    
    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        
        if(Name == "" and Email == "" and User == "" and Pass =="" ):
            messagebox.showinfo(title="Register Error", message="Não deixe nenhum campo vazio, preencha!")
        
        DataBaser.cursor.execute(''' INSERT INTO Users(Name, Email, User, Password) VALUES(?,?,?,?)
                                 ''' , (Name, Email, User, Pass))
        DataBaser.conn.commit()
        messagebox.showinfo(title="Register Info", message="Conta criada com sucesso")
    
    Register = ttk.Button(RightFrame, text="Register", width=20, command=RegisterToDataBase)
    Register.place(x=100, y=225)
    
    
    def BackToLogin():
        # Removendo Widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Traduzindo de volta os Widgets de login
        LoginButton.place(x=135)
        RegistreButton.place(x=135)
        
        
    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=100, y=260)
    
    
RegistreButton = ttk.Button(RightFrame, text="Registre", width=20, command=Register)
RegistreButton.place(x=135, y=230)

# ======================= Inicio  =======================
jan.mainloop()