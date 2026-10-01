import os
import pg8000
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv(dotenv_path=".env")


def obter_conexao():
    # Obtém uma conexão com o banco de dados PostgreSQL usando pg8000
    return pg8000.connect(
        user=os.getenv('user'),
        password=os.getenv('password'),
        host=os.getenv('host'),
        port=os.getenv('port'),
        database=os.getenv('database')
    )


def criar_tabela():
    # Cria tabela de produtos
    comando_sql = """
    CREATE TABLE IF NOT EXISTS produtos (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        preco DECIMAL(10, 2) NOT NULL
    );
    """
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(comando_sql)
            conn.commit()
    print("Tabela criada ou já existente!")

def criar_produto(nome, preco):
    # Cria produtos
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO produtos (nome, preco) VALUES (%s, %s) RETURNING id;", 
                (nome, preco)
            )
            id_gerado = cursor.fetchone()[0]
            conn.commit()
            return id_gerado

def listar_produtos():
    # Lista produtos
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nome, preco FROM produtos;")
            return cursor.fetchall()

def atualizar_produto(id_produto, novo_nome, novo_preco):
    # Atualiza um produto existente
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE produtos SET nome = %s, preco = %s WHERE id = %s;", 
                (novo_nome, novo_preco, id_produto)
            )
            conn.commit()

def deletar_produto(id_produto):
    # Deleta um produto
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM produtos WHERE id = %s;", (id_produto,))
            conn.commit()