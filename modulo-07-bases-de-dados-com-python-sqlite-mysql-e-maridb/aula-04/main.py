"""Aula 04 - Python sqlite3 + DB Brownser for SQLite"""
import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        # INSERT OR IGNORE - insere ou ignora em caso de erro
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        # UPDATE OR IGNORE - modifica ou ignora em caso de erro
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        # LIKE - igual a
        # %valor% - busca o valor em qualquer lugar no nome
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Leandro', '123456')
    # agenda.inserir('Maria', '111111')
    # agenda.inserir('João', '123457')
    # agenda.inserir('Rose', '123458')
    # agenda.inserir('Guilherme', '153456')
    # agenda.inserir('Fabrício', '124456')
    # agenda.listar()
    # agenda.editar('Francisco', '131313', 11)
    # agenda.listar()
    # agenda.excluir(11)
    agenda.inserir('Luiz Otávio', '102321')
    agenda.inserir('Luiz Felipe', '102322')
    agenda.inserir('Ronaldo Luiz', '102323')
    agenda.inserir('R. Luiza', '102325')
    agenda.inserir('R. Luiza meio do caminho', '102326')
    agenda.buscar('luiz')
