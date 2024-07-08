import streamlit as st
import pandas as pd
import sqlite3


# Conectar ao banco de dados SQLite
conn = sqlite3.connect('/mnt/projetos/scraping_ml/data/quotes.db')

# carregar os dados da tabela 'mercadolivre_tenis' em um DataFrame pandas
df = pd.read_sql_query('Select * from  mercadolivre_tenis', conn)

# Fechar conexão com o banco de dados
conn.close()

# Titulo da aplicação
st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')

# Melhorar o layout com colunas KPI's
st.subheader("KPI's principais do sistema")
col1,col2,col3 = st.columns(3)


# KPI 1: Numero total de itens
total_itens = df.shape[0]
col1.metric(label="Número total de Itens", value=total_itens)

# KPI 2: Numero de marcas únicas
unique_brands = df['brand'].nunique()
col2.metric(label="Número de Marcas únicas", value=unique_brands)

# KPI 3: Preço medio novo ( em reais)
average_new_price = df['new_price'].mean()
col3.metric(label='Preço Médio Novo (R$)', value=f'{average_new_price:.2f}')

# Quais Marcas são mais encontradas até a página 10
st.subheader('Marcas mais encontradas até a página 10')
col1,col2 = st.columns([4,2])
top_10_pages_brands = df    ['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

# Qual o preço medio por marca
st.subheader('Preço médio por marca')
col1,col2 = st.columns([4,2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
average_price_by_brand = df_non_zero_reviews.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)


# Qual a saisfação por marca
st.subheader('Satisfação por marca')
col1,col2 = st.columns([4,2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)