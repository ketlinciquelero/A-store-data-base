# tabelas
# clientes (id, nome, cpf, cidade, estado, bairro, rua, cep)
# produtos (id, nome, familia (eletronico, queijos, laticinios), codigo de barras)
# vendas (data da venda, cod barras, cpf cliente, quantidade, valor unitario, valor total)

import sqlite3
import arrow

ar = arrow.now().format('DD/MM/YYYY')
conexao = sqlite3.connect('lojadeprodutos.db')
cursor = conexao.cursor()


class LojadeProdutos:
    def __init__(self):
        dic = []

    def tabela_clientes(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
                       'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                       'cliente TEXT,'
                       'cpf TEXT,'
                       'cidade	TEXT,'
                       'estado TEXT,'
                       'bairro TEXT,'
                       'rua TEXT,'
                       'cep TEXT,'
                       'numero	TEXT)')
        conexao.commit()

    def tabela_produtos(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS produtos ('
                       'idProduto INTEGER PRIMARY KEY AUTOINCREMENT,'
                       'nomeProduto TEXT,'
                       'familia TEXT,'
                       'codigo_de_barras TEXT)')
        conexao.commit()

    def tabela_vendas(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS vendas ('
                       'idVenda INTEGER PRIMARY KEY AUTOINCREMENT,'
                       'data_da_venda TEXT,'
                       'codigo_de_barras TEXT,'
                       'cpf TEXT,'
                       'quantidade REAL,'
                       'valor_unitario REAL,'
                       'valor_total REAL)')
        conexao.commit()


loja = LojadeProdutos()

# loja.tabela_produtos()
# loja.tabela_vendas()
# loja.tabela_clientes()

cursor.close()
conexao.close()

