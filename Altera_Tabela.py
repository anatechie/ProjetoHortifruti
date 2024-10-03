import sqlite3 


con = sqlite3.connect('hortifruti.db')

try:
    cursor = con.cursor()
    cursor.execute("ALTER TABLE fornecedor ADD COLUMN Nome VARCHAR(50) NOT NULL")
    con.commit()
    print("Campo adicionado com sucesso!")
except sqlite3.Error as erro:
    con.rollback()
    print(f"Erro ao adicionar campo: {erro}")

    '''con.rollback() é chamado para desfazer as 
    alterações feitas no banco de dados, garantindo que o
      estado do banco de dados seja restaurado para o 
      estado anterior.'''