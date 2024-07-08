# scraping_ml

### Para rodar o web scraping 

#### para rodar o crawl da Coleta de fraldas
```
cd /scraping_ml/src/coleta_ml
scrapy crawl coleta_fralda_ml -o scraping_ml/data/data.json  
```

#### para rodar o crawl da Coleta de tenis
```
cd /scraping_ml/src/coleta_ml
scrapy crawl coleta_fralda_ml -o scraping_ml/data/data.json  

```

#### Para rodar o pandas para fazer as tranformações precisa estar dentro da pasta SRC
```
cd /scraping_ml/src/
python trasnsformacao/transform_fralda.py
python trasnsformacao/transform_tenis.py
```

Ao rodar o scrapping e as transformações você tera um banco de dados (quotes.db) <br>
Dentro do banco terá as 2 tabelas criadas:
* mercadolivre_fraldas
* mercadolivre_tenis 



#### para rodar o Streamlit precisa executar o comando abaixo dentro da pasta SRC
```
cd /scraping_ml/src/
streamlit run dashboard/app.py   

```