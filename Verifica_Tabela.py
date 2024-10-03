import sqlite3 


con = sqlite3.connect('hortifruti.db')
     
try:
    #verifica se as tabelas foram criadas
    cursor= con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # verica se as tabelas estão no bd
    #expected_tables define chamada de lista que contém os nomes das tabelas
    #que  devem estar no banco de dados
    expected_tables = ['cliente', 'funcionario', 'fornecedor', 'produto', 'estoque', 'venda', 'nfc']
    for table in expected_tables:
         #inicia loop de iteração para cada tabela na lista expected table
        if table not in [t[0] for t in tables]:
            ## verifica se a table atual(table) não está presente na lista de tabelas que foram encontradas no banco de dados(tables)
           #a expressão  [t[0] for t in tables]:  é uma lista de tuplas que contém os nomes das tabelas
            # a condição not in verifica se a tabela atual não está presente na lista de tabelas do bd
            print(f'Tabela {table} criada com sucesso!')
        else:
            print(f'Tabela {table} já existe!')
    
except sqlite3.Error as erro:
     print(f"Erro no banco de dados", {erro})

finally:
    if con:
     con.close()

#Sqlite_master é uma tabela mestra do sqlite contendo informações das tabelas dos bancos de dados
