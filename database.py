import sqlite3

# conexão e criação do banco de dados
def conectar_banco_de_dados():
    conn = sqlite3.connect('controle_financeiro.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_tabelas():
    conn, cursor = conectar_banco_de_dados()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS receitas
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        data TEXT NOT NULL, 
        valor REAL NOT NULL, 
        descricao TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS despesas
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        valor REAL NOT NULL,
        descricao TEXT
    )
    ''')

    conn.commit()
    conn.close()

criar_tabelas()
print('Tabelas criadas com sucesso!')
