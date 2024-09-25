import sqlite3

'''variavel de conexão com o bd'''
bd = sqlite3.connect('hortifruti.db')

'''criar tableta dentro do banco'''
'''objeto recebe objt onde foi criado o banco'''
cursor = bd.cursor()
'''atraves do obj horti que será digitado os comandos sql'''

'''comando que cria tabela'''
'''cursor.execute("""CREATE TABLE funcionario ( id integer primary key autoincrement,
              nome text not null, cpf integer not null, endereço text, dtnsc integer, 
             email text, cargo text not null, status text )""")'''

'''inserir dados na tabela'''
'''cursor.execute('INSERT INTO funcionario VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (nome, idade, cargo, salario, 
                                                                         data_admissao, departamento, email, telefone))
'''
cursor.execute('INSERT INTO funcionario VALUES("Maria", "12345678", "rua 7 lago sul", "08/12/2002","maria@gmail.com", "estoquista", "Ativo")')
'''commit confirmação dos dados inseridos'''
cursor.commit()