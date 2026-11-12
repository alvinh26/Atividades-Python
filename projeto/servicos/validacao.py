import sqlite3

def validar_cpf(cpf):
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()
        sql = "SELECT * FROM pacientes WHERE cpf = %s"
    except Exception as e:
        print(f"Erro ao validar CPF: {e}")    
    return cursor.execute(sql, (cpf)).fetchone()

def validar_telefone(telefone):
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()
        sql = "SELECT * FROM pacientes WHERE telefone = %s"
    except Exception as e:
        print(f"Erro ao validar telefone: {e}")    
    return cursor.execute(sql, (telefone)).fetchone()