 #Importando as bibliotecas
import pandas as pd
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt

# ============================================ #

# Conexão com o banco de dados
engine_dw = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/supermarket_dw"
)

print("Conexões estabelecidas com sucesso!")

# ============================================ #

# Captura dos dados da tabela SILVER para GOLD
df_gold = pd.read_sql(
    "SELECT * FROM silver s",
    engine_dw
)

print("Captura de dados da SILVER para GOLD concluida.")

# ============================================ #

# Qual filial apresentou o maior faturamento?
filial_faturamento = df_gold.groupby('filial')['valor_total'].sum().sort_values(ascending=False)

# GRAFICO - Qual filial apresentou o maior faturamento?
imagem_0 = 'resultados/graficos/faturamento_por_filial.png'
plt.figure(figsize=(10, 5))
plt.bar(filial_faturamento.index, filial_faturamento.values, color='#2b5c8f')
plt.title('Faturamento Total por Filial', fontsize=14)
plt.xlabel('Filial', fontsize=12)
plt.ylabel('Faturamento Total (R$)', fontsize=12)
plt.savefig(imagem_0, dpi=300, bbox_inches='tight')
plt.show()

# ============================================ #

# Qual filial realizou a maior quantidade de vendas?
filial_quantidade = df_gold.groupby('filial')['quantidade'].sum().sort_values(ascending=False)

# GRAFICO - Qual filial realizou a maior quantidade de vendas?
imagem_1 = 'resultados/graficos/faturamento_por_filial.png'
plt.figure(figsize=(10, 5))
plt.bar(filial_quantidade.index, filial_quantidade.values, color='#2b5c8f')
plt.title('Vendas por filial', fontsize=14)
plt.xlabel('Filial', fontsize=12)
plt.ylabel('Quantidade de vendas', fontsize=12)
plt.savefig(imagem_1, dpi=300, bbox_inches='tight')
plt.show()

# ============================================ #

# Qual linha de produto apresentou o maior faturamento?
produto_faturamento = df_gold.groupby('linha_produto')['valor_total'].sum().sort_values(ascending=False)

# GRAFICO - Qual linha de produto apresentou o maior faturamento?
imagem_2 = 'resultados/graficos/faturamento_por_produto.png'
plt.figure(figsize=(18, 7))
plt.bar(produto_faturamento.index, produto_faturamento.values, color='#2b5c8f')
plt.title('Faturamento por Linha de Produto', fontsize=14)
plt.xlabel('Linha de Produto', fontsize=12)
plt.ylabel('Faturamento Total (R$)', fontsize=12)
plt.savefig(imagem_2, dpi=300, bbox_inches='tight')
plt.show()

# ============================================ #

# Qual linha de produto recebeu a melhor avaliação média?
produto_avaliação = df_gold.groupby('linha_produto')['avaliação'].mean().sort_values(ascending=False)

# GRAFICO - Qual linha de produto recebeu a melhor avaliação média?
imagem_3 = 'resultados/graficos/avaliação_por_produto.png'
plt.figure(figsize=(18, 7))
plt.bar(produto_avaliação.index, produto_avaliação.values, color='#2b5c8f')
plt.title('Avaliação Média por Linha de Produto', fontsize=14)
plt.xlabel('Linha de Produto', fontsize=12)
plt.ylabel('Avaliação', fontsize=12)
plt.savefig(imagem_3, dpi=300, bbox_inches='tight')
plt.show()

# ============================================ #

# Qual foi a forma de pagamento mais utilizada?
forma_pagamento = df_gold.groupby('forma_pagamento')['forma_pagamento'].count().sort_values(ascending=False)

# GRAFICO - Qual foi a forma de pagamento mais utilizada?
imagem_4 = 'resultados/graficos/forma_pagamento.png'
plt.figure(figsize=(10, 5))
plt.bar(forma_pagamento.index, forma_pagamento.values, color='#2b5c8f')
plt.title('Forma de Pagamento mais utilizada', fontsize=14)
plt.xlabel('Forma de Pagamento', fontsize=12)
plt.ylabel('Quantidade Pedidos', fontsize=12)
plt.savefig(imagem_4, dpi=300, bbox_inches='tight')
plt.show()

# ============================================ #

# Qual foi o valor médio das vendas?
vendas_medio = df_gold['valor_total'].mean()

# GRAFICO - Qual foi o valor médio das vendas?
imagem_5 = 'resultados/graficos/valor_medio_vendas.png'
fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
ax.axis('off')
ax.text(0.5, 0.6, 'O VALOR MÉDIO DAS VENDAS FOI:', fontsize=14, ha='center', color='#555555')
ax.text(0.5, 0.3, f'R$ {vendas_medio:.2f}', fontsize=32, fontweight='bold', ha='center', color='#2b5c8f')
rect = plt.Rectangle((0.05, 0.05), 0.9, 0.9, fill=False, color='#cccccc', lw=1.5, transform=ax.transAxes)
ax.add_patch(rect)
plt.savefig(imagem_5, dpi=300, bbox_inches='tight')
plt.show()

# ============================================ #

# Qual foi a maior venda registrada?
vendas_maior = df_gold['valor_total'].max()

# GRAFICO - Qual foi a maior venda registrada?
imagem_6 = 'resultados/graficos/maior_venda.png'
fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
ax.axis('off')
ax.text(0.5, 0.6, 'A MAIOR VENDA REGISTRADA FOI:', fontsize=14, ha='center', color='#555555')
ax.text(0.5, 0.3, f'R$ {vendas_maior:.2f}', fontsize=32, fontweight='bold', ha='center', color='#2b5c8f')
rect = plt.Rectangle((0.05, 0.05), 0.9, 0.9, fill=False, color='#cccccc', lw=1.5, transform=ax.transAxes)
ax.add_patch(rect)
plt.savefig(imagem_6, dpi=300, bbox_inches='tight')
plt.show()

# ============================================ #

# Em qual dia da semana ocorreu a maior quantidade de vendas ?
dia_semana = df_gold.groupby('dia_da_semana')['pedido'].count().sort_values(ascending=False)

# GRAFICO - Em qual dia da semana ocorreu a maior quantidade de vendas ?
imagem_7 = 'resultados/graficos/venda_dia_semana.png'
plt.figure(figsize=(10, 5))
plt.bar(dia_semana.index, dia_semana.values, color='#2b5c8f')
plt.title('Vendas por Dia da Semana', fontsize=14)
plt.xlabel('Dia da Semana', fontsize=12)
plt.ylabel('Quantidade Vendas', fontsize=12)
plt.savefig(imagem_7, dpi=300, bbox_inches='tight')
plt.show()

# ============================================ #

# Gravando o DataFrame na tabela GOLD do banco de dados
df_gold.to_sql(
    "gold",
    engine_dw,
    schema="public",
    if_exists="replace",
    index=False
)

print ("Dados tratados gravados com sucesso na tabela GOLD")

print (">>> Pipeline de ESTATISTICAS executado com sucesso! <<<")