from mysql.connector import Error, pooling

DB_PARAMS = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'imc_python',
    'charset': 'utf8mb4',
    'time_zone': '-03:00',
    'use_pure': True,
    'connect_timeout': 10
}

_pool = pooling.MySQLConnectionPool(
    pool_name= 'imc_pool',
    pool_size= 5,
    **DB_PARAMS
)

def get_connection():
    try:
        return _pool.get_connection()
    except Error as e:
        raise Exception(f'Erro ao obter conexão do pool: {e}')


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

def verificar_criar_tabela():
    sql_teste = "SHOW TABLES LIKE 'calculos'"
    resultado = execute_query(sql_teste, fetch=True)

    if not resultado:
        print("Tabela de calculos não encontrada! Criando a tabela...")

        sql = '''
                CREATE TABLE IF NOT EXISTS calculos(
                    id_calculo BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    peso DECIMAL(6,2) NOT NULL,
                    altura DECIMAL(5,2) NOT NULL,
                    imc DECIMAL(5,2) NOT NULL,
    
                    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    alterado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    deletado_em DATETIME NULL
                );
                '''
        resultado = execute_query(sql, fetch=True)
        print("Tabela criada com sucesso!")

    else:
        print("Tabela calculos já existe! Bora jogar campeão...")