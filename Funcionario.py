import customtkinter
import random
import mysql.connector

connection = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '<senha>',
    database = '<nome do banco>')

cursor = connection.cursor()
comando2 = cursor.execute("CREATE TABLE IF NOT EXISTS FUNCIONÁRIO(MATRICULA VARCHAR(15), NOME VARCHAR(255), IDADE VARCHAR(5), NASCIMENTO VARCHAR(15), ESTADO_CIVIL VARCHAR(15), CPF VARCHAR(15), RG VARCHAR(15), ENDEREÇO VARCHAR(255), CRM_COREN VARCHAR(15), CONTRATO VARCHAR(15), CARGO VARCHAR(255));")
connection.commit()



def cad_funcionario():
    global nome_Entry, idade_Entry, nascimento_Entry, estado_civil_Entry, cpf_Entry, rg_Entry, cep_Entry, logadouro_Entry, bairro_Entry, cidade_Entry, uf_Entry, crm_Entry, cargo_Entry
    home = customtkinter.CTk()
    home.title("Cadastrar funcionário")
    home.geometry("800x600")
    texto_nome = customtkinter.CTkLabel(home, text="Digite o seu nome:")
    texto_nome.pack()
    nome_Entry = customtkinter.CTkEntry(home, placeholder_text="Seu nome", corner_radius=2)
    nome_Entry.pack()
    text_idade = customtkinter.CTkLabel(home, text="Insira sua idade:")
    text_idade.pack()
    idade_Entry = customtkinter.CTkEntry(home, placeholder_text="Sua idade", corner_radius=2)
    idade_Entry.pack()
    text_nasci = customtkinter.CTkLabel(home, text="Insira sua data de nascimento:")
    text_nasci.pack()
    nascimento_Entry = customtkinter.CTkEntry(home, placeholder_text="Data de nascimento", corner_radius=2)
    nascimento_Entry.pack()
    estado_civil = customtkinter.CTkLabel(home, text="Estado civil do funcionario:")
    estado_civil.pack()
    estado_civil_Entry = customtkinter.CTkEntry(home, placeholder_text="", corner_radius=2)
    estado_civil_Entry.pack()
    text_cpf = customtkinter.CTkLabel(home, text="Insira seu CPF:")
    text_cpf.pack()
    cpf_Entry = customtkinter.CTkEntry(home, placeholder_text="cpf", corner_radius=2)
    cpf_Entry.pack()
    rg_text = customtkinter.CTkLabel(home, text="Preencha com seu rg:")
    rg_text.pack()
    rg_Entry = customtkinter.CTkEntry(home, placeholder_text="RG",corner_radius=2)
    rg_Entry.pack()
    text_cep = customtkinter.CTkLabel(home, text="Digite seu cep aqui:")
    text_cep.pack()
    cep_Entry = customtkinter.CTkEntry(home, placeholder_text="CEP", corner_radius=2)
    cep_Entry.pack()
    text_logadouro = customtkinter.CTkLabel(home, text="DIgite o logadouro:")
    text_logadouro.pack()
    logadouro_Entry = customtkinter.CTkEntry(home, placeholder_text="Logadouro", corner_radius=2)
    logadouro_Entry.pack()
    text_numero = customtkinter.CTkLabel(home, text="Número da casa")
    text_numero.pack()
    numero_Entry = customtkinter.CTkEntry(home, placeholder_text="Número", corner_radius=2)
    numero_Entry.pack()
    text_bairro = customtkinter.CTkLabel(home, text="Insira o nome do bairro:")
    text_bairro.pack()
    bairro_Entry = customtkinter.CTkEntry(home, placeholder_text="Bairro", corner_radius=2)
    bairro_Entry.pack()
    text_cidade = customtkinter.CTkLabel(home, text="Digite o nome da sua cidade:")
    text_cidade.pack()
    cidade_Entry = customtkinter.CTkEntry(home, placeholder_text="Cidade", corner_radius=2)
    cidade_Entry.pack()
    text_uf = customtkinter.CTkLabel(home, text="Digite sua uf, exemplo: PE")
    text_uf.pack()
    uf_Entry = customtkinter.CTkEntry(home, placeholder_text="UF", corner_radius=2)
    uf_Entry.pack()
    text_crm = customtkinter.CTkLabel(home, text="Digite aqui seu crm ou corem:")
    text_crm.pack()
    crm_Entry = customtkinter.CTkEntry(home, placeholder_text="CRM", corner_radius=2)
    crm_Entry.pack()
    text_cargo = customtkinter.CTkLabel(home, text="Digite o nome do cargo a ser preenchido: ")
    text_cargo.pack()
    cargo_Entry = customtkinter.CTkEntry(home, placeholder_text="Cargo:", corner_radius=2)
    cargo_Entry.pack()
    bt = customtkinter.CTkButton(home, text="Salvar", command=salvar_cad_f)
    bt.pack()
    home.mainloop()

def atualizar_funcionario():
    home = customtkinter.CTk()
    home.title("Atualizar cadastro")
    home.mainloop()

def deletar_funcionario():
    global matricula_Entry
    home = customtkinter.CTk()
    home.title("Deletar cadastro")
    texto = customtkinter.CTkLabel(home, text="Digite o número da matricula para deletar: ")
    texto.pack()
    matricula_Entry = customtkinter.CTkEntry(home, placeholder_text="Matricula", corner_radius=2)
    matricula_Entry.pack()
    bt = customtkinter.CTkButton(home, text="Apagar", command=delet_func)
    bt.pack()
    home.mainloop()

def delet_func():
    matricula = matricula_Entry.get()
    cursor.execute(f'DELETE FROM FUNCIONÁRIO WHERE MATRICULA = "{matricula}";')
    connection.commit()

def visu_funcionario():
    home = customtkinter.CTk()
    home.title("Visualizar")
    home.mainloop()

def salvar_cad_f():
    contrato = random.randint(30000, 40000)
    matricula = random.randint(15000,25000)
    nome = nome_Entry.get()
    idade = idade_Entry.get()
    nascimento = nascimento_Entry.get()
    estado_civil = estado_civil_Entry.get()
    cpf = cpf_Entry.get()
    rg = rg_Entry.get()
    cep = cep_Entry.get()
    logadouro = logadouro_Entry.get()
    bairro = bairro_Entry.get()
    cidade = cidade_Entry.get()
    uf = uf_Entry.get()
    crm = crm_Entry.get()
    cargo = cargo_Entry.get()
    endereco = cep, logadouro, bairro, cidade, uf
    cursor.execute (f'INSERT INTO FUNCIONÁRIO VALUES("{matricula}","{nome}","{idade}","{nascimento}","{estado_civil}","{cpf}","{rg}","{endereco}","{crm}","{contrato}","{cargo}")')
    connection.commit()