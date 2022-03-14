"""Aula 07: CRUD com Pymysql no MySQL e Mariadb Server"""
from contextlib import contextmanager
import pymysql.cursors

# CRUD - CREATE, READ, UPDATE and DELETE


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        print('Conexão fechada')
        conexao.close()

# INSERE UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()

# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 19, 55),
#             ('JOSÉ', 'FIGUEIREDO', 19, 55),
#         ]
#
#         # executemany - executa vários registros
#         cursor.executemany(sql, dados)
#         conexao.commit()

# DELETA UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (8,))
#         conexao.commit()

# Deleta quantidade determinada de registros
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

# DELETE REGISTROS ENTRE UM RANGE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 15))
#         conexao.commit()

# ATUALIZA UM REGISTRO NA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE  clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('Luciano', 5))
        conexao.commit()

# SELECIONA O DADOS DA BASE DE DADOS
with conecta() as conexao:  # gerenciador de contexto responsável por fechar a conexão automaticamente
    with conexao.cursor() as cursor:  # gerenciador de contexto responsável por fechar o cursor automaticamente
        # LIMIT - define o número máximo de itens a serem coletados
        # ORDER BY x DESC / ASC - ordena os resultado pelo campo x em uma ordem decrescente ou ascendente
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
