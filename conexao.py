'''Criar banco de dados'''
import sqlite3 
con = sqlite3.connect('hortifruti.db')

'''criar tabelas'''
sql_cliente = '''
CREATE TABLE IF NOT EXISTS cliente(
id_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
Nome VARCHAR(50) NOT NULL,
Sobrenome VARCHAR(40) NOT NULL,
RG VARCHAR(12) NOT NULL,
CPF VARCHAR(12) NOT NULL,
Telefone VARCHAR (12),
Endereco VARCHAR(100),
Data_Nascimento DATE NOT NULL,
Email VARCHAR (20),
id_funcionario  INTEGER NOT NULL REFERENCES funcionario(id_funcionario)

);
'''
sql_produto = '''
CREATE TABLE IF NOT EXISTS produto(
id_Produto INTEGER PRIMARY KEY AUTOINCREMENT,
Nome_Produto VARCHAR(50) NOT NULL,
Preco DECIMAL(10,2) NOT NULL,
Tipo_Produto VARCHAR(20),
Peso VARCHAR (10),
Quantidade INTEGER NOT NULL,
Descricao VARCHAR(100),
id_Cliente INTEGER (10) REFERENCES cliente(id_Cliente)
);
'''

sql_venda = '''
CREATE TABLE IF NOT EXISTS venda(
id_Venda INTEGER PRIMARY KEY AUTOINCREMENT,
Quantidade INTEGER NOT NULL,
Preco DECIMAL(10,2) NOT NULL,
Nota_Fiscal SMALLINT NOT NULL,
id_Produto INTEGER NOT NULL REFERENCES produto(id_Produto),
id_Cliente INTEGER NOT NULL REFERENCES cliente(id_Cliente)
);
'''

sql_funcionario = '''
CREATE TABLE IF NOT EXISTS funcionario(
id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
Nome VARCHAR(50) NOT NULL,
Sobrenome VARCHAR(50) NOT NULL,
CPF VARCHAR (12) NOT NULL,
Endereco VARCHAR(40),
Telefone VARCHAR(12),
Cargo VARCHAR(20),
Status VARCHAR(10),
id_Cliente INTEGER (10) NOT NULL REFERENCES  cliente(id_Cliente),
id_Produto  INTEGER (10) NOT NULL REFERENCES produto(id_Produto),
id_NFC   INTEGER (10) NOT NULL REFERENCES nfc(id_NFC)

);
'''

sql_estoque = '''
CREATE TABLE IF NOT EXISTS estoque(
id_Estoque INTEGER PRIMARY KEY AUTOINCREMENT,
Qnt_Produto SMALLINT NOT NULL,
Preco_Compra DECIMAL(10,2),
Preco_Venda DECIMAL(10,2),
Tipo_produto VARCHAR(15),
id_Produto INTEGER NOT NULL REFERENCES produto(id_Produto),
id_funcionario INTEGER NOT NULL REFERENCES funcionario(id_funcionario)

);
'''

sql_nfc = '''
CREATE TABLE IF NOT EXISTS nfc(
id_NFC INTEGER PRIMARY KEY AUTOINCREMENT,
Nota_Fiscal SMALLINT NOT NULL,
Data_Compra DATETIME,
id_Cliente INTEGER NOT NULL REFERENCES cliente(id_Cliente),
id_Produto INTEGER NOT NULL  REFERENCES produto(id_Produto),
id_funcionario INTEGER NOT NULL REFERENCES funcionario(id_funcionario)

);
'''

'''MANIPULAR EXCEÇÕES TRY/EXCEPT/FINALLY'''
'''cursor executa os comandos sql dentro do banco'''
try:
    '''as tabelas ainda não estão persistidas nesse passo, para que a persistencia ocorra, é necessário o comando commit()'''
    cursor = con.cursor()
    #cursor.execute(sql_cliente)
    #con.commit()
    #print('Tabela cliente criada com sucesso!')
    cursor.execute(sql_produto)
    con.commit()
    print('Tabela produto criada com sucesso!')
    cursor.execute(sql_funcionario)
    con.commit()
    print('Tabela funcionario criada com sucesso!')
    cursor.execute(sql_estoque)
    con.commit()
    print('Tabela estoque criada com sucesso!')
    cursor.execute(sql_nfc)
    con.commit()
    print('Tabela nfc criada com sucesso!')
    cursor.execute(sql_venda)
    con.commit()
    print('Tabela venda criada com sucesso!')
except con.DatabaseError as erro:
    print(f'Erro ao criar tabelas: {erro}')
finally:
    if con:
        con.close()



