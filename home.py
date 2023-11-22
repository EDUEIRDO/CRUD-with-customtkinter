import customtkinter

from paciente import *

from funcionario import *

from agendamentos import *


def fechar():
    principal.destroy()
    


def for_paciente():
    home = customtkinter.CTk()
    home.title("Para pacientes")
    home.geometry()
    texto = customtkinter.CTkLabel(home, text=" utilize o menu para navegar pelo sistema!")
    texto.pack()
    opc1 = customtkinter.CTkButton(home, text="Cadastrar paciente", command=cad_paciente)
    opc1.pack()
    opc2 = customtkinter.CTkButton(home, text="Atualizar cadastro", command=atualizar_paciente)
    opc2.pack()
    opc3 = customtkinter.CTkButton(home, text="deletar cadastro", command=deletar_paciente)
    opc3.pack()
    opc4 = customtkinter.CTkButton(home, text="visualizar cadastro", command=visu_paciente)
    opc4.pack()
    home.mainloop()

def for_funcionarios():
    home = customtkinter.CTk()
    home.title("Para funcionários")
    opc1 = customtkinter.CTkButton(home, text="Cadastrar funcionário", command=cad_funcionario)
    opc2 = customtkinter.CTkButton(home, text="Atualizar cadastro", command=atualizar_funcionario)
    opc3 = customtkinter.CTkButton(home, text="Deletar cadastro", command=deletar_funcionario)
    opc4 = customtkinter.CTkButton(home, text="Visualizar", command=visu_funcionario)
    opc1.pack()
    opc2.pack()
    opc3.pack()
    opc4.pack()
    home.mainloop()

def for_agendamento():
    home = customtkinter.CTk()
    home.title("Agendamento ")
    opc1 = customtkinter.CTkButton(home, text="Agendamento de consultas", command=agendamento_consulta)
    opc2 = customtkinter.CTkButton(home, text="Agendamento de exames", command=agendar_exame)
    opc1.pack()
    opc2.pack()
    home.mainloop()

principal = customtkinter.CTk()
principal.title("Menu")
principal.geometry("300x200")
texto = customtkinter.CTkLabel(principal, text="Seja bem-vindo ao Take Care by CDGM,\n  utilize os botões para navegar pelo sistema!")
texto.pack()
bt1 = customtkinter.CTkButton(principal, text="Pacientes", command=for_paciente)
bt1.place(x=80, y=30)
bt2 = customtkinter.CTkButton(principal, text="funcionários", command=for_funcionarios)
bt2.place(x=80, y=65)
bt3 = customtkinter.CTkButton(principal, text="Agendamento", command=for_agendamento)
bt3.place(x=80, y=100)
bt4 = customtkinter.CTkButton(master = principal, text="fechar programa", command=fechar).place(x=80, y=135)
principal.mainloop()
