import numpy as np
import pandas as pd

dfOriginal = pd.read_json('ecommerce-events.ndjson', lines = True)

# Separa o dataframe com eventtype Search
bolSearch = dfOriginal.eventType == 'search'
dfSearch = dfOriginal[bolSearch]

# Dataframe somente com produtos
bolProduct = dfOriginal.eventType == 'product'
dfProduct = dfOriginal[bolProduct]

# contador de queries
countSearch = dfSearch['query'].value_counts()

def returnCount(qry):
    return countSearch[qry]

dfSearch['numSearch'] = dfSearch['query'].apply(returnCount)

# Dataframe somente com pesquisas com 15 ou mais repetições
dfSearch15 = dfSearch[dfSearch.numSearch >= 15]

# Converte o produto para string
def strProduct(prod):
    return str(int(prod))

dfProduct['productStr'] = dfProduct['product'].apply(strProduct)

# Tentei converter a lista de itens retornados pela pesquisa para tupla, 
# para facilitar a busca, porém não consegui fazer a busca, mas essa função funciona
def tupleItems(lista):
    if isinstance(lista, list):
        return tuple(lista)

dfSearch15['tupleItems'] = dfSearch15['searchItems'].apply(tupleItems)


# Verificando se a URL do Search encontra um produto com mesmo Referrer
dfSearch15['click'] = (dfSearch15['url'].isin(dfProduct['referrer']))
# dfSearch15['click'] = (dfSearch15['tupleItems'].isin(dfProduct['productStr']))
# & (dfProduct['productStr'].isin(dfSearch15['tupleItems']))


# Apresentando a lista dos 5 mais
dfSearch15[dfSearch15['click'] == True]['query'].value_counts().head()