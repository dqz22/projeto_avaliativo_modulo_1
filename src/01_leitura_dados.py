#Importando as bibliotecas
import pandas as pd
from sqlalchemy import create_engine, text

# ============================================ #

# Conexão com o banco de dados
engine_dw = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/supermarket_dw"
)

print("Conexões estabelecidas com sucesso!")

# ============================================ #

# Verificando se o banco de dados foi realmente criado
admin_engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
)

for db_name in ["supermarket_dw"]:
    with admin_engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        if not conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = 'supermarket_dw'")
        ).scalar():
            conn.execute(text("CREATE DATABASE supermarket_dw"))
            print("Banco 'supermarket_dw' criado.")
        else:
            print("Banco 'supermarket_dw' já existe.")

# ============================================ #

# Criando os tabelas
with engine_dw.begin() as conn:
    conn.execute(text("CREATE TABLE raw()"))
    conn.execute(text("CREATE TABLE bronze()"))
    conn.execute(text("CREATE TABLE silver()"))
    conn.execute(text("CREATE TABLE gold()"))

print("Tabelas RAW, BRONZE, SILVER E GOLD criadas no banco de dados 'supermarket_dw'.")

# ============================================ #

# Lendo o arquivo CSV e salvando em uma variavel
df = pd.read_csv('data/raw/supermarket.csv')
print ("Leitura de dados do arquivo CSV concluida!")

# ============================================ #

# Gravando os dados brutos do arquivo no banco de dados na tabela RAW
df.to_sql(
    "raw",
    engine_dw,
    schema="public",
    if_exists="replace",
    index=False
)

print ("Dados brutos do arquivo CSV gravados com sucesso na tabela RAW")

# ============================================ #

# Gravando os dados brutos do arquivo no banco de dados na tabela BRONZE
df.to_sql(
    "bronze",
    engine_dw,
    schema="public",
    if_exists="replace",
    index=False
)

print ("Dados brutos do arquivo CSV gravados com sucesso na tabela BRONZE")
print (">>> Pipeline da LEITURA de dados executado com sucesso! <<<")