# CRUD Practice with Supabase

This repository contains a simple Python application that demonstrates basic CRUD (Create, Read, Update, Delete) operations on a PostgreSQL database, specifically one hosted on Supabase.

## About The Project

The project is structured to separate database logic from the main application flow. It uses the `pg8000` library to connect to the database and `python-dotenv` to manage environment variables for database credentials.

### Core Functionality

*   **Database Connection**: Establishes a connection to a PostgreSQL database using credentials from a `.env` file.
*   **Table Creation**: Creates a `produtos` (products) table if it doesn't already exist.
*   **Create**: Adds new products to the `produtos` table.
*   **Read**: Lists all products from the table.
*   **Update**: Modifies the name and price of an existing product.
*   **Delete**: Removes a product from the table by its ID.

## Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

*   Python 3.x
*   A Supabase account with an active project. You will need the database connection details (user, password, host, port, database name).

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/vixtorzzz/crud-practice-supabase.git
    cd crud-practice-supabase
    ```

2.  **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file** in the root of the project directory and add your Supabase database credentials. You can find these details in your Supabase project's dashboard under `Project Settings` > `Database`.

    ```ini
    # .env file
    user="postgres"
    password="YOUR_DATABASE_PASSWORD"
    host="YOUR_DATABASE_HOST"
    port="YOUR_DATABASE_PORT"
    database="postgres"
    ```

## Usage

The `main.py` script serves as the entry point to demonstrate the functionality. It initializes the database table, creates a new product, and then lists all products.

To run the application:
```sh
python main.py
```

The output will be:
```
--- Iniciando ---
Produtos cadastrados: [(1, 'Headset', Decimal('35.50'))]
```

You can modify `main.py` or use the functions from `db_helper.py` in your own scripts to perform other operations like updating or deleting products.

### Available Functions in `db_helper.py`

*   `criar_tabela()`: Creates the `produtos` table.
*   `criar_produto(nome, preco)`: Inserts a new product.
*   `listar_produtos()`: Returns a list of all products.
*   `atualizar_produto(id_produto, novo_nome, novo_preco)`: Updates a product specified by its ID.
*   `deletar_produto(id_produto)`: Deletes a product specified by its ID.
