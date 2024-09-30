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
Email VARCHAR (20)

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
FOREIGN KEY (id_Cliente) REFERENCES cliente(id_Cliente)
);
'''

sql_venda = '''
CREATE TABLE IF NOT EXISTS venda(
id_Venda INTEGER PRIMARY KEY AUTOINCREMENT,
Quantidade INTEGER NOT NULL,
Preco DECIMAL(10,2) NOT NULL,
Nota_Fiscal SMALLINT NOT NULL,
FOREIGN KEY (id_Cliente) REFERENCES cliente(id_Cliente),
FOREIGN KEY (id_Produto) REFERENCES produto(id_Produto)
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
Cargo VARCHAR(20)
Status Varchar(10)
);
'''

sql_estoque = '''
CREATE TABLE IF NOT EXISTS estoque(
id_Estoque INTEGER PRIMARY KEY AUTOINCREMENT,
Qnt_Produto SMALLINT NOT NULL,
Preco_Compra DECIMAL(10,2),
Preco_Venda DECIMAL(10,2),
Tipo_produto VARCHAR(15)
)
'''

sql_nfc = '''
CREATE TABLE IF NOT EXISTS nfc(
id_NFC INTEGER PRIMARY KEY AUTOINCREMENT,
Nota_Fiscal SMALLINT NOT NULL,
id_Cliente INTEGER NOT NULL,
id_Produto INTEGER NOT NULL,
Data_Compra DATETIME,
FOREIGN KEY (id_Produto) REFERENCES produto(id_Produto),
FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario),
FOREIGN KEY (id_Cliente) REFERENCES cliente(id_Cliente)
)
'''

'''MANIPULAR EXCEÇÕES TRY/EXCEPT/FINALLY'''
'''cursor executa os comandos sql dentro do banco'''
try:
    '''as tabelas ainda não estão persistidas nesse passo, para que a persistencia ocorra, é necessário o comando commit()'''
    cursor = con.cursor()
    cursor.execute(sql_cliente)
    cursor.execute(sql_funcionario)
    cursor.execute(sql_estoque)
    cursor.execute(sql_nfc)
    cursor.execute(sql_venda)
    con.commit()
except con.DatabaseError as erro:
    print(f'Erro ao criar tabelas: {erro}')
finally:
    if con:
        con.close()

