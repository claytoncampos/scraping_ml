import pandas as pd
import sqlite3
from datetime import datetime

# Definir o caminho para o arquivo JSONL

df = pd.read_json('../../data/fralda.jsonl', lines=True)

# setar o pandar para mostrar todas as colunas

pd.options.display.max_columns = None

# Adicionar a coluna _source com um valor fixo

df['source'] = 'https://lista.mercadolivre.com.br/fralda'

# Adicionar a coluna _data_coleta com data e hora atuais

df['_data_coleta'] = datetime.now()

print(df)

# Tratar os valores Nulos para colunas numericas e de texto
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)


# Remover os parenteses das colunas 'reviews_amount' e tanformar ele em inteiro
df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_amount']= df['reviews_amount'].fillna(0).astype(int)


# Tratar os preços como float e calcular os valores totais
df['old_price'] = df['old_price_reais'] + (df['old_price_centavos'] / 100)
df['new_price'] = df['new_price_reais'] + (df['new_price_centavos'] / 100)

# Remover as colunas antigas de preços

df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)


# Conectar ao banco de dados SQLite (ou criar um novo)

conn = sqlite3.connect('../../data/quotes.db')

# Salvar o DataFrame no banco de dados SQLite

df.to_sql('mercadolivre_fraldas', conn, if_exists='replace', index=False)

# Fechar conexao com banco de dados
conn.close()

print(df.head())
