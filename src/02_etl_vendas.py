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

# Captura dos dados da tabela RAW para DataFrames 
df_silver = pd.read_sql(
    "SELECT * FROM bronze b",
    engine_dw
)

print("Captura de dados da BRONZE para DataFrame concluida.")

# ============================================ #

# Renomeando o nome das colunas
df_silver = df_silver.rename(
    columns=
        {"Invoice ID": "pedido",
        "Branch": "filial",
        "City": "cidade",
        "Customer type": "tipo_cliente",
        "Gender": "genero",
        "Product line": "linha_produto",
        "Unit price": "preco_unitario",
        "Quantity": "quantidade",
        "Tax 5%": "imposto_5%",
        "Sales": "valor_total",
        "Date": "data_venda",
        "Time": "hora_venda",
        "Payment": "forma_pagamento",
        "cogs": "custo_mercadoria",
        "gross margin percentage": "margem_bruta_percentual",
        "gross income": "receita_bruto",
        "Rating": "avaliação"}
        )

print("Ação para renomear as colunas concluida!")

# ============================================ #

# Convertendo os dados de DATA e HORARIO
df_silver["data_venda"] = pd.to_datetime(df_silver["data_venda"])
df_silver["hora_venda"] = pd.to_datetime(df_silver["hora_venda"])
df_silver["hora_venda"] = df_silver["hora_venda"].dt.time

print("Conversão dos dados da coluna de DATA e HORARIO concluida!")

# ============================================ #

# Criando a coluna DIA_DA_SEMANA 
dias = {
    0: 'Segunda-feira',
    1: 'Terça-feira',
    2: 'Quarta-feira',
    3: 'Quinta-feira',
    4: 'Sexta-feira',
    5: 'Sábado',
    6: 'Domingo'
}

df_silver['dia_da_semana'] = df_silver['data_venda'].dt.dayofweek.map(dias)

print("Coluna 'dia_da_semana' criada com sucesso!")

# ============================================ #

# Deixar todas as letras maiusculas

df_silver["filial"] = df_silver["filial"].str.upper()
df_silver["cidade"] = df_silver["cidade"].str.upper()
df_silver["tipo_cliente"] = df_silver["tipo_cliente"].str.upper()
df_silver["genero"] = df_silver["genero"].str.upper()
df_silver["linha_produto"] = df_silver["linha_produto"].str.upper()
df_silver["forma_pagamento"] = df_silver["forma_pagamento"].str.upper()

print("Padronização das letras para Maiusculo concluida!")

# ============================================ #

# Gravando o DataFrame na tabela SILVER do banco de dados
df_silver.to_sql(
    "silver",
    engine_dw,
    schema="public",
    if_exists="replace",
    index=False
)

print ("Dados tratados gravados com sucesso na tabela SILVER")

# ============================================ #

# Criando o arquivo CSV Tratado e salvando na pasta "processed"
df_silver.to_csv("data/processed/supermarket_tratado.csv")

print("Arquivo 'supermarket_tratados.csv' gerado com sucesso!")
print (">>> Pipeline de ETL dos dados executado com sucesso! <<<")