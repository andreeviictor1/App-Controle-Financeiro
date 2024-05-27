import pandas as pd
from database import conectar_banco_de_dados

def adicionar_receita(data, valor, descricao):
    conn, cursor = conectar_banco_de_dados()
    cursor.execute('''
                   INSERT INTO receitas(data, valor, descricao) VALUES(?, ?, ?)''', (data, valor, descricao))
    conn.commit()
    conn.close()

def adicionar_despesa(data, valor, descricao):
    conn, cursor = conectar_banco_de_dados()
    cursor.execute('''
                   INSERT INTO despesas(data, valor, descricao) VALUES(?, ?, ?)''', (data, valor, descricao))
    conn.commit()
    conn.close()

def visualizar_receitas():
    conn, cursor = conectar_banco_de_dados()
    cursor.execute('SELECT * FROM receitas')
    receitas = cursor.fetchall()
    conn.close()
    return receitas

def visualizar_despesas():
    conn, cursor = conectar_banco_de_dados()
    cursor.execute('SELECT * FROM despesas')
    despesas = cursor.fetchall()
    conn.close()
    return despesas

def atualizar_receita(id, data, valor, descricao):
    conn, cursor = conectar_banco_de_dados()
    cursor.execute('''
                   UPDATE receitas SET data = ?, valor = ?, descricao = ? WHERE id = ? ''', (data, valor, descricao, id))
    conn.commit()
    conn.close()

def atualizar_despesa(id, data, valor, descricao):
    conn, cursor = conectar_banco_de_dados()
    cursor.execute('''
                   UPDATE despesas SET data = ?, valor = ?, descricao = ? WHERE id = ? ''', (data, valor, descricao, id))
    conn.commit()
    conn.close()

def deletar_receita(id):
    conn, cursor = conectar_banco_de_dados()
    cursor.execute('''
                   DELETE FROM receitas WHERE id = ? ''', (id,))
    conn.commit()
    conn.close()

def deletar_despesa(id):
    conn, cursor = conectar_banco_de_dados()
    cursor.execute('''
                   DELETE FROM despesas WHERE id = ? ''', (id,))
    conn.commit()
    conn.close()

def gerar_relatorio():
    conn, cursor = conectar_banco_de_dados()

    receitas_df = pd.read_sql_query('SELECT * FROM receitas', conn)
    despesas_df = pd.read_sql_query('SELECT * FROM despesas', conn)

    total_receitas = receitas_df['valor'].sum()
    total_despesas = despesas_df['valor'].sum()

    saldo_final = total_receitas - total_despesas

    relatorio = {
        'Total de Receitas': total_receitas,
        'Total de Despesas': total_despesas,
        'Saldo Final': saldo_final
    }

    conn.close()
    
    return relatorio
