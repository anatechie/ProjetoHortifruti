import sqlite3 as con 

try:
    conecta = con.connect('hortifruti.db')
    cursor = conecta.cursor()

    #verifica se as tabelas foram criadas
    res = cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="cliente"')
    res = cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="funcionario"')
    res = cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="estoque"')
    res = cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="venda"')
    res = cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="nfc"')
    print(res.fetchall())
except con.DatabaseError as erro:
      print("Erro no banco de dados", erro)
finally:
    if conecta:
     conecta.close()

#Sqlite_master é uma tabela mestra do sqlite contendo informações das tabelas dos bancos de dados
