import os
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Busca a variável DB_URI
DB_URI = os.getenv('DB_URI')

def obter_conexao():
    if not DB_URI:
        raise ValueError("Erro: A variável de ambiente DB_URI não foi configurada!")
    return psycopg2.connect(DB_URI)

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

# --- OPERAÇÕES DO CRUD ---

def criar_produto(nome, preco):
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
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nome, preco FROM produtos;")
            return cursor.fetchall()

def atualizar_produto(id_produto, novo_nome, novo_preco):
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE produtos SET nome = %s, preco = %s WHERE id = %s;", 
                (novo_nome, novo_preco, id_produto)
            )
            conn.commit()

def deletar_produto(id_produto):
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM produtos WHERE id = %s;", (id_produto,))
            conn.commit()