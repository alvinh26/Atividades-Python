import psycopg2

def criar_conexao():
    try:
        conexao = psycopg2.connect(
            host = "localhost",
            database = "farmacia",
            user = "postgres",
            password = "pipoquinha",
            port = "5432"
        )
        return conexao
    except Exception as e:
        print(f"Erro de conexão: {e}")