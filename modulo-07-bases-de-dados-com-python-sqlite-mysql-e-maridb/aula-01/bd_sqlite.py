"""Aula 01: SQLite usando o módulo sqlite3"""

import sqlite3

conexao = sqlite3.connect('basededados.db')  # cria o banco de dados ou acessa um banco já existente
cursor = conexao.cursor()  # o cursor que fará as alterações no banco

# cursor.execute() serve para inserir comandos SQL no banco
# CREATE TABLE IF NOT EXISTS - cria uma tabela com o nome informado, caso já existir a tabela, esse comando é pulado
# INTEGER - define o tipo da coluna como do tipo inteiro
# PRIMARY KEY - define como chave primária os valores da coluna, dessa forma eles nunca serão valores iguais
# AUTOINCREMENT - toda nova inserção na tabela clientes, fará com que essa coluna seja incrementada automaticamente
# TEXT - define o tipo da coluna como tipo texto
# REAL - define o tipo da coluna como tipo float
# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')
#
# # INSERT INTO insere valores na tabela clientes
# # () - são colocados os nomes das colunas que terã́o os valores inseridos
# # VALUES () - são colocados os valores que serão inseridos nas colunas por justaposição
# # cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Luiz Otávio", 80.5)')  # isso faz SQL injection
#
# # utilizando o (?, ?) é possível inserir valores através de uma tupla
# # deste modo se previne o problema de SQL injection
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
#
# # utilizando (:nomecoluna, :nomecoluna) é possível inserir valores apartir de um dicionário
# # esse modo támbem previne o SQL injection
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#     {'nome': 'Joãozinho', 'peso': 25})
#
# # outra forma de se inserir é omitindo o (nome, peso), mas dessa forma é necessário informar após o VALUES todas as
# # colunas existentes na tabela
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)',
#     {'id': None, 'nome': 'Daniel', 'peso': 113})
#
# # conexao.commit()  # Faz com que o comando acima seja executado na base de dados
# conexao.commit()

# # o comando abaixo vai atualizar o valor do nome na tabela clientes onde o id for igual o informado
# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'nome': 'Joana', 'id': 2}
# )
# conexao.commit()
#
# # o comando abaixo exclui a linha conforme o id
# # sempre ao utilizar o DELETE tenha muito cuidado, pois isso pode comprometer o seu banco se usado de forma errada
# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {'id': 2}
# )
#
# conexao.commit()

cursor.execute(
    'SELECT nome, peso FROM clientes WHERE peso > :peso',
    {'peso': 50}
)

for linha in cursor.fetchall():
    nome, peso = linha

    print(nome, peso)


# # SELECT * FROM - seleciona todos os valores da tabela
# cursor.execute('SELECT * FROM clientes')
#
# # cursor.fetchall() - coleta todos os valores selecionados anteriormente no comando SELECT
# for linha in cursor.fetchall():  # imprime no console os valores de todas as linhas na tabela
#     identificador, nome, peso = linha  # desempacota os valores da linha em variáveis
#     print(identificador, nome, peso)

cursor.close()  # sempre depois de usar o cursor é uma convenção fechar ele no final da sua utilização
conexao.close()  # sempre depois de usar a conexão é uma convenção fechar ela no final da sua utilização
