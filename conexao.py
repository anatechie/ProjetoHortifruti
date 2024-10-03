import sqlite3 as con

insere_cliente = '''
INSERT INTO cliente(Nome, Sobrenome, RG, CPF, Telefone, Endereco, Data_Nascimento, Email, id_funcionario)
VALUES ("Ana", "Rodrigues", "12345678", "12345678910", "Rua 7", "5561999999999", "2024-12-08", "ana@hotmail.com", 1);
'''

insere_produto = '''
INSERT INTO cliente(Nome, Preco, Tipo_Produto, Peso, Quantidade, Descricao)
VALUES ("Manga", "5,37",  "Fruta", "0,5", "10", "Manga verde");

'''

insere_venda = '''
INSERT INTO cliente(Quantidade, Preco, Nota_Fiscal)
VALUES ("1", "5,37",  "123456");

'''

insere_funcionario = '''
INSERT INTO cliente(Nome, Sobrenome, CPF, Endereço, Telefone, Cargo, Status)
VALUES ("Breno", "Ferreira", "12333466666", "Quadra 314", "98342384",  "Caixa", "Ativo");

'''

insere_fornecedor = '''
INSERT INTO cliente(CNPJ, Telefone, Endereco, Email, Nome)
VALUES ("22455434", "40028922", "Rua paraiso", "adaoeva@gmail.com", "Adão e Eva Hortifrutigranjeiro");
'''

insere_estoque= '''
INSERT INTO cliente(Qntd_Produto, Preco_Compra, Preco_Venda, Tipo_Produto)
VALUES ("12", "64,44",  "5,37", "Fruta");

'''

insere_nfc = '''
INSERT INTO cliente(id_NFC, id_Cliente, id_Produto, Data_Compra)
VALUES ("54", "633", "21", "2024-10-03");
'''

try: 
    conexao = con.connect('hortifruti.db')
    cursor = conexao.cursor()

    cursor.execute(insere_cliente)
    cursor.execute(insere_produto)
    cursor.execute(insere_venda)
    cursor.execute(insere_funcionario)
    cursor.execute(insere_fornecedor)
    cursor.execute(insere_estoque)
    cursor.execute(insere_nfc)

    conexao.commit()
    print('Dados inseridos com sucesso')
except con.Error as erro:
    print(f'Erro ao inserir dados: {erro}')
else:
    res =cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()
