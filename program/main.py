import pyodbc
import os

def connect() -> bool:

    try:
        global connection
        connection = pyodbc.connect(
            driver = "{SQL Server}",
            server = "regulus.cotuca.unicamp.br",
            database = "gmacedo",
            uid = "gmacedo",
            pwd = "gmacedo"
        )
        return True
    except:
        return False
    
def insert() -> bool:

    # cursor é um objeto que permite que nosso programa execute comandos SQL lá no servidor
    os.system('cls')
    connection = ''
    cursor = connection.cursor()
    codigoProduto = int(input("Código ------ "))
    nome = input("Nome -------- ")
    preco = float(input("Preço ------- "))
    
    try:
        # tentar executar o comando no banco de dados
        cursor.execute("INSERT INTO pratica.Produto(codigoProduto, nome, preco, inativo) VALUES" + f"({codigoProduto}, '{nome}', {preco}, 0)")
        # aplicar as alterações no banco de dados
        cursor.commit()
        return True
    except:
        # em caso de erro
        return False
    
def update() -> bool:

    pass

def delete() -> bool:

    pass

def select() -> bool:

    pass
    
@click.command("menu")
@click.version_option("0.1.0", prog_name = "mercadinho")
def menu():

    click.echo("Test")

    # abriu a conexão com o banco de dados
    if connect():
        
        option = -1

        while option != 0:
            # os.system('cls')
            print("0 - Sair")
            print("1 - Cadastrar um produto")
            print("2 - Alterar um produto")
            print("3 - Excluir um produto")
            print("4 - Listar os produtos")
            option = int(input("\nDigite a opção desejada: "))

            if option == 1:
                insert()
            elif option == 2:
                update()
            elif option == 3:
                delete()
            elif option == 4:
                select()

        connection.close()

if __name__ == "__main__":

    menu()