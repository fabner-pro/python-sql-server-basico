import pymssql
from config import server, database, username, password

def connect_to_sqlserver():
    """
    Função para conectar ao SQL Server usando pymssql (sem ODBC).
    """
    try:
        conn = pymssql.connect(
            server=server,
            user=username,
            password=password,
            database=database
        )
        print("Conexão com SQL Server estabelecida com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao SQL Server: {e}")
        return None

if __name__ == "__main__":
    conn = connect_to_sqlserver()
    if conn:
        # Aqui você pode adicionar operações com o banco, como executar queries
        conn.close()
        print("Conexão fechada.")