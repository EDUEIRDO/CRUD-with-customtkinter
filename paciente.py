import customtkinter

import random
import mysql.connector

connection = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '<senha>',
    database = '<nome do banco>')

cursor = connection.cursor()
comando1 = cursor.execute("CREATE TABLE IF NOT EXISTS PACIENTE(PRONTUARIO VARCHAR(15), CONVENIO VARCHAR(15), NOME VARCHAR(255), IDADE VARCHAR(5), NASCIMENTO VARCHAR(15), CPF VARCHAR(15) ,RG VARCHAR(15), ENDEREÇO VARCHAR(255));")
connection.commit()

def cad_paciente():
    global convenio_Entry, nome_Entry, idade_Entry, nascimento_Entry, cpf_Entry, nascimento_Entry, rg_Entry, cep_Entry, logadouro_Entry, numero_Entry, bairro_Entry, cidade_Entry, uf_Entry
    home = customtkinter.CTk()
    home.geometry("800x600")
    home.title("Cadastro de pacientes")
    texto = customtkinter.CTkLabel(home, text="Para cadastrar o paciente é necessario preencher os campos a seguir:")
    texto.pack()
    text_con = customtkinter.CTkLabel(home, text="Digite o número do convenio:")
    text_con.pack()
    convenio_Entry = customtkinter.CTkEntry(home, placeholder_text="convenio", corner_radius=2)
    convenio_Entry.pack()
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
    
    bt = customtkinter.CTkButton(home, text="Salvar", command=salvar_cad_p)
    bt.pack()
    home.mainloop()



def atualizar_paciente():
    global prontuario_Entry, convenio_Entry
    home = customtkinter.CTk()
    home.title("Cadastro de pacientes")
    home.geometry("800x600")
    texto = customtkinter.CTkLabel(home, text="Atenção! as informações serão atualizadas a partir do prontuario do paciente,\ncaso o mesmo esteja duplicado ou com númeração errada é recomendado a exclusão de tais informações.")
    texto.pack()
    text_prontuario = customtkinter.CTkLabel(home, text="Primeiramente digite o número do prontuario para identificação:")
    text_prontuario.pack()
    prontuario_Entry = customtkinter.CTkEntry(home, placeholder_text="prontuario", corner_radius=2)
    prontuario_Entry.pack()
    text2 = customtkinter.CTkLabel(home, text="Atenção, preencha somente o que desejar atualizar e aperte no botão. ")
    text2.pack()
    convenio_Entry = customtkinter.CTkEntry(home, placeholder_text="convenio", corner_radius=2)
    convenio_Entry.pack()
    opc1 = customtkinter.CTkButton(home, text="Atualizar convenio", command=comando1)
    opc1.pack()
    nome_Entry = customtkinter.CTkEntry(home, placeholder_text="Seu nome", corner_radius=2)
    nome_Entry.pack()
    opc2 = customtkinter.CTkButton(home, text="Atualizar nome")
    opc2.pack()
    idade_Entry = customtkinter.CTkEntry(home, placeholder_text="Sua idade", corner_radius=2)
    idade_Entry.pack()
    opc3 = customtkinter.CTkButton(home, text="Atualizar idade")
    opc3.pack()
    nascimento_Entry = customtkinter.CTkEntry(home, placeholder_text="Data de nascimento", corner_radius=2)
    nascimento_Entry.pack()
    opc4 = customtkinter.CTkButton(home, text="Atualizar data")
    opc4.pack()
    cpf_Entry = customtkinter.CTkEntry(home, placeholder_text="cpf", corner_radius=2)
    cpf_Entry.pack()
    opc5 = customtkinter.CTkButton(home, text="Atualizar cpf")
    opc5.pack()
    rg_Entry = customtkinter.CTkEntry(home, placeholder_text="RG",corner_radius=2)
    rg_Entry.pack()
    opc6 = customtkinter.CTkButton(home, text="Atualizar rg")
    opc6.pack()
    cep_Entry = customtkinter.CTkEntry(home, placeholder_text="CEP", corner_radius=2)
    cep_Entry.pack()
    opc7 = customtkinter.CTkButton(home, text="")
    opc7.pack()
    logadouro_Entry = customtkinter.CTkEntry(home, placeholder_text="Logadouro", corner_radius=2)
    logadouro_Entry.pack()
    opc8 = customtkinter.CTkButton(home, text="")
    opc8.pack()
    numero_Entry = customtkinter.CTkEntry(home, placeholder_text="Número", corner_radius=2)
    numero_Entry.pack()
    opc9 = customtkinter.CTkButton(home, text="")
    opc9.pack()
    bairro_Entry = customtkinter.CTkEntry(home, placeholder_text="Bairro", corner_radius=2)
    bairro_Entry.pack()
    opc10 = customtkinter.CTkButton(home, text="")
    opc10.pack()
    cidade_Entry = customtkinter.CTkEntry(home, placeholder_text="Cidade", corner_radius=2)
    cidade_Entry.pack()
    opc11 = customtkinter.CTkButton(home, text="")
    opc11.pack()
    uf_Entry = customtkinter.CTkEntry(home, placeholder_text="UF", corner_radius=2)
    uf_Entry.pack()
    opc12 = customtkinter.CTkButton(home, text="")
    opc12.pack()

    home.mainloop()



def comando1():
    convenio = convenio_Entry.get()
    prontuario = prontuario_Entry.get()
    cursor.execute(f'UPDATE PACIENTE SET  CONVENIO = "{convenio}" WHERE PRONTUARIO = "{prontuario}"')
    connection.commit()



    

def deletar_paciente():
    global prontuario_Entry 
    home = customtkinter.CTk()
    home.title("Deletar paciente")
    texto = customtkinter.CTkLabel(home, text="Preencha o campo abaixo para excluir um paciente!")
    texto.pack()
    prontuario_Entry = customtkinter.CTkEntry(home, placeholder_text="Número do prontuario", fg_color="transparent")
    prontuario_Entry.pack()
    bt = customtkinter.CTkButton(home, text="Apagar", command=delet_pac)
    bt.pack()
    home.mainloop()


def visu_paciente():
    home = customtkinter.CTk()
    home.title("Cadastro de pacientes")
    text = customtkinter.CTkLabel(home,)
    text.pack()
    cursor.execute("Select * From PACIENTE;")

    home.mainloop()

def salvar_cad_p():
    prontuario_Entry = random.randint(1000,10000)
    convenio = convenio_Entry.get()
    nome = nome_Entry.get() 
    idade = idade_Entry.get()
    nascimento = nascimento_Entry.get()
    cpf = cpf_Entry.get()
    rg = rg_Entry.get()
    cep = cep_Entry.get()
    logadouro = logadouro_Entry.get()
    bairro = bairro_Entry.get()
    cidade = cidade_Entry.get()
    uf = uf_Entry.get()
    endereco = cep, logadouro, bairro, cidade, uf
    cursor.execute(f'INSERT INTO PACIENTE VALUES("{prontuario_Entry}","{convenio}","{nome}","{idade}","{nascimento}","{cpf}","{rg}","{endereco}");')
    connection.commit()

def delet_pac():
    prontuario = prontuario_Entry.get()
    cursor.execute(f'DELETE  FROM PACIENTE WHERE PRONTUARIO = "{prontuario}";')
    connection.commit()