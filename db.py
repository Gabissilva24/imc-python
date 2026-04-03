import mysql.connector
from mysql.connector import Error

CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'aula_flask',
    'charset': 'utf8mb4'
}

def get_connection():
    """Retorna uma conexão ativa com o banco. Levanta Exception em caso de falha."""
    try:
        return mysql.connector.connect(**CONFIG)
    except Error as e:
        raise Exception(f'Não foi possível conectar ao banco: {e}')


def execute_query(sql, params=None, fetch=False):
    conn = get_connection()
    try:
        # dictionary=True: cada linha retorna como dicionário — produto['nome'] em vez de produto[0]
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, params or ())

        if fetch:
            return cursor.fetchall()   # retorna todas as linhas
        else:
            conn.commit()              # confirma a transação
            return cursor.rowcount     # número de linhas afetadas

    except Error as e:
        conn.rollback()  # desfaz alterações parciais em caso de erro
        raise Exception(f'Erro ao executar query: {e}')
    finally:
        cursor.close()
        conn.close()


def execute_one(sql, params=None):
    """
    Executa um SELECT e retorna apenas a primeira linha (ou None).
    Útil para buscar um registro por ID.
    """
    resultados = execute_query(sql, params, fetch=True)
    return resultados[0] if resultados else None
