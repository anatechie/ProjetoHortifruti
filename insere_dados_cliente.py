import sqlite3 as con 
from rich.console import Console 
from rich.table import Table
from conexao import criar_conexao  # Importe a função de conexão

console = Console()

def insere_cliente(cursor):
    insere_cliente = '''
    INSERT INTO cliente(Nome, Sobrenome, RG, CPF, Telefone, Endereco, Data_Nascimento, Email, id_funcionario)
    VALUES("Ana", "Rodrigues", "12345678", "12345678910", "Rua 7", "5561999999999", "2024-12-08", "ana@hotmail.com", 1);
    '''
    try:
        cursor.execute(insere_cliente)
        console.print("[green]CLIENTE inserido com sucesso![/green]")
    except con.DatabaseError as erro: 
        console.print(f'[red]Erro ao inserir cliente: {erro} [/red]')

'''Conectar ao bd e executar as funções'''
try: 
    conexao = criar_conexao()  # Use a função de conexão importada
    cursor = conexao.cursor()

    # Verificação das tabelas diretamente no código principal
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    expected_tables = ['cliente', 'funcionario', 'fornecedor', 'produto', 'estoque', 'venda', 'nfc']
    for table in expected_tables:
        if table not in [t[0] for t in tables]:
            print(f'Tabela {table} criada com sucesso!')
        else:
            print(f'Tabela {table} já existe!')

    insere_cliente(cursor)

    conexao.commit()
    console.print('[dark green]Dados inseridos com sucesso![/dark green]')

except con.Error as erro:
    console.print(f'[dark red]Erro ao inserir dados: {erro}[/dark red]')

else: 
    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = res.fetchall()
    table_display = Table(title="Tabelas no Banco de Dados")
    table_display.add_column("Nome da Tabela", justify="left", style="cyan", no_wrap=True)
    for t in tables:
        table_display.add_row(t[0])
    console.print(table_display)

finally:
    if conexao:
        cursor.close()
        conexao.close()
        console.print("[yellow]Conexão finalizada.[/yellow]")


'''import sqlite3 as con 
from rich.console import Console 
from rich.table import Table


console = Console()

def insere_cliente(cursor):
    insere_cliente = '''
    #INSERT INTO cliente(Nome, Sobrenome, RG, CPF, Telefone, Endereco, Data_Nascimento, Email, id_funcionario)
   # VALUES("Ana", "Rodrigues", "12345678", "12345678910", "Rua 7", "5561999999999", "2024-12-08", "ana@hotmail.com", 1);
    
    #try:
      #  cursor.execute(insere_cliente)
        #console.print("[green]CLIENTE inserido com sucesso![/green]")
  #  except con.DatabaseError as erro: 
    #    console.print(f'[red]Erro ao inserir cliente: {erro} [/red]')

'''try: 
    conexao = con.connect('hortifruti.db')
    cursor = conexao.cursor()

    insere_cliente(cursor)

    conexao.commit()
    console.print('[dark green]Dados inseridos com sucesso![/dark green]')

except con.Error as erro:
    console.print(f'[dark red]Erro ao inserir dados: {erro}[/dark red]')

else: 
    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = res.fetchall()
    table_display = Table(title="Tabelas no Banco de Dados")
    table_display.add_column("Nome da Tabela", justify="left", style="cyan", no_wrap=True)
    for t in tables:
        table_display.add_row(t[0])
    console.print(table_display)

finally:
    if conexao:
        cursor.close()
        conexao.close()
        console.print("[yellow]Conexão finalizada.[/yellow]")

Console = console() cria instancia console para permitir a impressão de mensagens 
formatadas no terminal.

Função inserir_cliente define função para inserir um cliente na tablea cliente

bloco try tenta executar a instrução SQL. Except captura e imprime erros de bd
 
bloco try conexao = con.connect tenta conectar ao banco e criar obj cursor
 commit confirma as alterações

 Bloco except imprime erros se ocorrerem
 Else: executa se n houver exceção. Recupera e imprime os nomes das tabelas no bd 

 finaly fecha conexao
'''
