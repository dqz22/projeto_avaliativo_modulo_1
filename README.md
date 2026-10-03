📊 Projeto Avaliativo — Módulo 1
📌 Sobre o Projeto

Este projeto tem como objetivo desenvolver um pipeline introdutório de análise de dados, utilizando PostgreSQL, SQL, Python, Pandas, Estatística Descritiva e Git/GitHub.

O projeto foi estruturado com base no conceito de Arquitetura Medallion, utilizando diferentes etapas de maturidade dos dados: Raw, Bronze, Silver e Gold.

O fluxo desenvolvido contempla desde a ingestão dos dados brutos até o tratamento, transformação, análise exploratória e geração de informações para responder às perguntas de negócio.

🏗️ Fluxo do Projeto

supermarket.csv
       │
       ▼
data/raw/supermarket.csv
       │
       ▼
PostgreSQL — supermarket_dw
       │
       ├── RAW
       └── BRONZE
              │
              ▼
       Python + Pandas
       │
       │ Tratamento e transformação
       │
       ▼
PostgreSQL — supermarket_dw
       │
       ├── SILVER
       └── GOLD
              │
              ▼
data/processed/supermarket_tratado.csv
              │
              ▼
     Estatística Descritiva
              │
       ┌──────┴──────┐
       ▼             ▼
resultados/      resultados/
estatisticas/    graficos/

🗃️ Fonte dos Dados

Os dados utilizados no projeto foram obtidos por meio do Kaggle:

Supermarket Sales Dataset

https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales

A base original está no formato CSV, delimitada por vírgulas, contendo dados numéricos, textos, datas e horários que necessitam de tratamento antes da realização das análises.

🥇 Arquitetura dos Dados

O projeto utiliza uma estrutura inspirada na Arquitetura Medallion, separando os dados conforme seu nível de tratamento:

🟫 RAW

Armazena os dados exatamente como foram obtidos na fonte original.

🟤 BRONZE

Recebe os dados brutos no banco de dados, servindo como etapa intermediária para o processo de transformação.

⚪ SILVER

Contém os dados tratados e padronizados, incluindo:

Renomeação das colunas;
Tradução dos nomes das colunas do inglês para o português;
Conversão de textos para formatos de data e horário;
Criação da coluna referente ao dia da semana;
Padronização dos textos em letras maiúsculas;
Verificações de dados nulos e duplicados.
🟡 GOLD

Etapa destinada à utilização dos dados tratados para realização das análises e geração dos resultados.

📂 Estrutura do Projeto

```
📦 projeto-avaliativo
│
├── 📁 data
│   ├── 📁 raw
│   │   └── supermarket.csv
│   │
│   └── 📁 processed
│       └── supermarket_tratado.csv
│
├── 📁 sql
│   ├── 01_criar_banco.sql
│   ├── 02_criar_tabelas.sql
│   └── 03_consultas.sql
│
├── 📁 src
│   ├── 01_leitura_dados.py
│   ├── 02_etl_vendas.py
│   └── 03_estatisticas.py
│
├── 📁 resultados
│   ├── 📁 estatisticas
│   │   └── projeto_avaliativo.ipynb
│   │
│   └── 📁 graficos
│
├── README.md
├── requirements.txt
└── .gitignore
```

🗄️ Scripts SQL

01_criar_banco.sql

Cria o banco de dados supermarket_dw, utilizado para armazenar os dados durante as diferentes etapas do projeto.

02_criar_tabelas.sql

Cria as tabelas utilizadas no processo, representando os diferentes estágios de maturidade dos dados.

03_consultas.sql

Realiza consultas utilizando comandos e funções SQL, como:

SELECT
WHERE
GROUP BY
SUM
AVG
🐍 Scripts Python
01_leitura_dados.py

Responsável pela primeira etapa do pipeline:

Importação das bibliotecas pandas e sqlalchemy;
Conexão com o PostgreSQL;
Verificação da existência do banco de dados;
Criação das tabelas;
Leitura do arquivo CSV;
Armazenamento dos dados em um DataFrame;
Inserção dos dados nas tabelas RAW e BRONZE.
02_etl_vendas.py

Responsável pelo processo de ETL e tratamento dos dados.

Principais etapas:

Captura dos dados da tabela BRONZE;
Armazenamento no DataFrame df_silver;
Renomeação e tradução das colunas;
Conversão de texto para data e horário;
Criação da coluna com o dia da semana;
Padronização dos textos em letras maiúsculas;
Gravação dos dados tratados na tabela SILVER;
Exportação dos dados tratados para:
data/processed/supermarket_tratado.csv
03_estatisticas.py

Responsável pela análise dos dados:

Captura dos dados da tabela SILVER;
Armazenamento no DataFrame df_gold;
Aplicação de conceitos de estatística descritiva;
Resolução das perguntas de negócio;
Geração dos gráficos;
Salvamento das imagens em:
resultados/graficos/
📈 Perguntas de Negócio

A etapa de análise exploratória foi desenvolvida para responder às perguntas propostas no projeto avaliativo.

1. Qual filial apresentou o maior faturamento?

Resposta: A filial GIZA apresentou o maior faturamento.

2. Qual filial realizou a maior quantidade de vendas?

Resposta: A filial ALEX realizou a maior quantidade de vendas.

3. Qual linha de produto apresentou o maior faturamento?

Resposta: FOOD AND BEVERAGES apresentou o maior faturamento.

4. Qual linha de produto recebeu a melhor avaliação média?

Resposta: FOOD AND BEVERAGES apresentou a melhor avaliação média.

5. Qual foi a forma de pagamento mais utilizada?

Resposta: EWALLET foi a forma de pagamento mais utilizada.

6. Qual foi o valor médio das vendas?

Resposta: O valor médio das vendas foi de R$ 322,97.

7. Qual foi a maior venda registrada?

Resposta: A maior venda registrada foi de R$ 1.042,65.

8. Em qual dia da semana ocorreu a maior quantidade de vendas?

Resposta: Sábado apresentou a maior quantidade de vendas.

🛠️ Tecnologias Utilizadas
🐍 Python
🐼 Pandas
🗄️ PostgreSQL
🔤 SQL
📊 Matplotlib
📓 Jupyter Notebook
🌱 Git
🐙 GitHub
▶️ Como Executar o Projeto

1. Instalar as dependências

As bibliotecas necessárias estão listadas no arquivo:

requirements.txt

Instale as dependências com:

pip install -r requirements.txt
2. Configurar o PostgreSQL

Crie o banco de dados utilizando o script:

sql/01_criar_banco.sql

Em seguida, execute:

sql/02_criar_tabelas.sql

para criar as tabelas utilizadas no pipeline.

3. Executar a ingestão dos dados

Execute:

python src/01_leitura_dados.py

Esse processo realiza a leitura do CSV e insere os dados nas etapas RAW e BRONZE.

4. Executar o processo de ETL

Execute:

python src/02_etl_vendas.py

O script realiza o tratamento e a transformação dos dados, armazenando o resultado na camada SILVER e gerando o arquivo tratado.

5. Executar a análise

Por fim:

python src/03_estatisticas.py

O script realiza a análise estatística e gera os gráficos utilizados para responder às perguntas de negócio.

📊 Resultados

Os resultados das análises são disponibilizados em:

resultados/estatisticas/

e os gráficos gerados pelo pipeline ficam armazenados em:

resultados/graficos/

O notebook projeto_avaliativo.ipynb também é utilizado para validar o processo e apresentar a estatística descritiva utilizada na análise.

🎯 Conclusão

O projeto permitiu desenvolver um fluxo completo e introdutório de análise de dados, partindo da ingestão de uma base CSV, passando pelo armazenamento no PostgreSQL, tratamento e transformação com Python e Pandas, até chegar à análise estatística e visualização dos resultados.

Além da aplicação prática de Python, SQL e Pandas, o projeto também possibilitou trabalhar com organização de dados, estruturação de pipeline, arquitetura Medallion e controle de versão utilizando Git e GitHub.

### Desenvolvido por

**Diego Queiroz**

📌 Data Analytics | Python | SQL | Pandas | PostgreSQL
