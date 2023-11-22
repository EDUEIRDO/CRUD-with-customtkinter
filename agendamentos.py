import customtkinter
import mysql.connector
import random
connection = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '<senha>',
    database = '<nome do banco>')

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS CONSULTAS(COD_CONSULTA VARCHAR(15), PRONTUARIO VARCHAR(15), NOME VARCHAR(255), IDADE VARCHAR(5), CRM VARCHAR(15), COD_ESPECIALIDADE VARCHAR(5), VALOR_CONSULTA VARCHAR(20), DATA_CONSULTA VARCHAR(15), HORARIO_CONSULTA VARCHAR(15));")
connection.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS EXAMES(COD_EXAME VARCHAR(15), PRONTUARIO VARCHAR(15), PACIENTE VARCHAR(255), IDADE VARCHAR(5), TIPO VARCHAR(255), VALOR_EXAME VARCHAR(15), DATA_EXAME VARCHAR(15) , HORARIO_EXAME VARCHAR(15))")
connection.commit()

def at_consulta():
    print("sas")

def dele_consul():
    print("Deletando")

def visu():
    print("Ainda n consegui")

def agendar_exame():
    home = customtkinter.CTk()
    home.title("Agendamento de exames")
    home.mainloop()


def ag_consulta():
    global prontuario_Entry, nome_consulta_Entry, idade_consulta_Entry, crm_Entry, cod_especialidade_Entry, valor_consulta_Entry, horario_consulta_Entry, data_consulta_Entry
    home = customtkinter.CTk()
    home.title("Agendamento de consultas")
    home.geometry("800x600")
    texto = customtkinter.CTkLabel(home, text="Insira")
    texto.pack()
    prontuario_Entry = customtkinter.CTkEntry(home, placeholder_text="Prontuario", corner_radius=2)
    prontuario_Entry.pack()
    texto2 = customtkinter.CTkLabel(home, text="Insira")
    texto2.pack()
    nome_consulta_Entry = customtkinter.CTkEntry(home, placeholder_text="Nome", corner_radius=2)
    nome_consulta_Entry.pack()
    texto3 = customtkinter.CTkLabel(home, text="Insira")
    texto3.pack()
    idade_consulta_Entry = customtkinter.CTkEntry(home, placeholder_text="Idade", corner_radius=2)
    idade_consulta_Entry.pack()
    texto4 = customtkinter.CTkLabel(home, text="Insira")
    texto4.pack()
    crm_Entry = customtkinter.CTkEntry(home, placeholder_text="CRM", corner_radius=2)
    crm_Entry.pack()
    texto5 = customtkinter.CTkLabel(home, text="Insira")
    texto5.pack()
    cod_especialidade_Entry = customtkinter.CTkEntry(home, placeholder_text="Especialidade", corner_radius=2)
    cod_especialidade_Entry.pack() 
    texto6 = customtkinter.CTkLabel(home, text="Insira")
    texto6.pack()
    valor_consulta_Entry = customtkinter.CTkEntry(home, placeholder_text="Valor", corner_radius=2)
    valor_consulta_Entry.pack()
    texto7 = customtkinter.CTkLabel(home, text="Insira")
    texto7.pack()
    horario_consulta_Entry = customtkinter.CTkEntry(home, placeholder_text="Horario", corner_radius=2)
    horario_consulta_Entry.pack()
    texto8 = customtkinter.CTkLabel(home, text="Insira")
    texto8.pack()
    data_consulta_Entry = customtkinter.CTkEntry(home, placeholder_text="Data", corner_radius=2)
    data_consulta_Entry.pack()
    bt_save = customtkinter.CTkButton(home, text="Salvar", command=save_agendamento)
    bt_save.pack()
    home.mainloop()


def save_agendamento():
    cod_consultas = random.randint(100,999)
    pront = prontuario_Entry.get()
    nome_c= nome_consulta_Entry.get()
    idade_c = idade_consulta_Entry.get()
    crm = crm_Entry.get()
    cod_esp = cod_especialidade_Entry.get()
    valor_c = valor_consulta_Entry.get()
    horario_c= horario_consulta_Entry.get()
    data_c = data_consulta_Entry.get()
    cursor.execute (f'INSERT INTO  CONSULTAS VALUES("{cod_consultas}","{pront}","{nome_c}","{idade_c}","{crm}","{cod_esp}","{valor_c}","{horario_c}", "{data_c}");')
    connection.commit()



def agendamento_consulta():
    home = customtkinter.CTk()
    home.title("Agendamentos de consultas")
    home.geometry("800x600")
    opc1 = customtkinter.CTkButton(home, text="Agendar consultas", command=ag_consulta)
    opc1.pack()
    opc2 = customtkinter.CTkButton(home, text="Atualizar consultas", command=at_consulta)
    opc2.pack()
    opc3 = customtkinter.CTkButton(home, text="Deletar consultas", command=dele_consul)
    opc3.pack()
    opc4 = customtkinter.CTkButton(home, text="Visualizar consultas", command=visu)
    opc4.pack()
    home.mainloop()