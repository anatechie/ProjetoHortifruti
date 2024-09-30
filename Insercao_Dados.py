import sqlite3 as con

insere_cliente = '''
INSERT INTO cliente(Nome, Sobrenome, RG, CPF, Telefone, Endereço, Data_Nascimento, Email)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
'''

insere_produto = '''
INSERT INTO cliente(Nome, Preco, Tipo_Produto, Peso, Quantidade, Descricao)
VALUES (?, ?, ?, ?, ?, ?)
'''

insere_venda = '''
INSERT INTO cliente(Quantidade, Preco, Nota_Fiscal)
VALUES (?, ?, ?)
'''

insere_funcionario = '''
INSERT INTO cliente(Nome, Sobrenome, CPF, Endereço, Telefone, Cargo, Status)
VALUES (?, ?, ?, ?, ?, ?, ?)
'''

insere_estoque= '''
INSERT INTO cliente(Qntd_Produto, Preco_Compra, Preco_Venda, Tipo_Produto)
VALUES (?, ?, ?, ?)
'''

insere_nfc = '''
INSERT INTO cliente(id_NFC, id_Cliente, id_Produto, Data_Compra)
VALUES (?, ?, ?, ?)
'''

try: 
    conexao = con.connect('hortifruti.db')
    cursor = conexao.curor()

    cursor.execute(insere_cliente)
    cursor.execute(insere_produto)
    cursor.execute(insere_venda)
    cursor.execute(insere_funcionario)
    cursor.execute(insere_estoque)
    cursor.execute(insere_nfc)

    conexao.commit()
    print('Dados inseridos com sucesso')
except con.Error as erro:
    print(f'Erro ao inserir dados: {erro}')
else:
    res =cursor.execute("SELECT * FROM Cliente;")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()
