from config.db import criar_conexao
from servicos.validacao import validar_cpf, validar_telefone

def inserir_paciente(nome: str, endereco: str, telefone: str, cpf: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        sql = "INSERT INTO paciente (nome, endereco, telefone, cpf) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, endereco, telefone, cpf))
        conexao.commit()

        print("Paciente inserido com sucesso!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conexao.close()

def cadastro_paciente(nome: str, endereco: str, telefone: str, cpf: str):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    sql = "SELECT * FROM paciente WHERE nome = %s AND endereco = %s AND cpf = %s AND telefone = %s"
    cursor.execute(sql, (nome, endereco, cpf, telefone))
    pacientes = cursor.fetchone()
    cursor.close()
    conexao.close()
    return pacientes