import sqlite3 


con = sqlite3.connect('hortifruti.db')
     
try:
    #verifica se as tabelas foram criadas
    cursor= con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # verica se as tabelas estão no bd
    expected_tables = ['cliente', 'funcionario', 'produto', 'estoque', 'venda', 'nfc']
    for table in expected_tables:
        if table not in [t[0] for t in tables]:
            print(f'Tabela {table} criada com sucesso!')
        else:
            print(f'Tabela {table} criada com sucesso!')
    
except sqlite3.Error as erro:
     print(f"Erro no banco de dados", {erro})

finally:
    if con:
     con.close()

#Sqlite_master é uma tabela mestra do sqlite contendo informações das tabelas dos bancos de dados
