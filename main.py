# main.py
from db_helper import criar_tabela, criar_produto, listar_produtos

def rodar():
    print("--- Iniciando ---")
    # criar_tabela()
    
    criar_produto("Teclado Mecânico", 200.00)
    
    produtos = listar_produtos()
    print(f"Produtos cadastrados: {produtos}")

if __name__ == "__main__":
    rodar()
