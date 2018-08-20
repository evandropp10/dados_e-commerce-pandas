import numpy as np
import pandas as pd
import seaborn as sns
%matplotlib inline

dfOriginal = pd.read_json('ecommerce-events.ndjson', lines = True)

# Dataframe de transações
bolTrans = (dfOriginal.eventType == 'transaction')
dfTrans = dfOriginal[bolTrans]

# Separa o dataframe de produtos da campanha 2
bolCamp2 = (dfOriginal.utm_campaign == 'Campaign_2') & (dfOriginal.eventType == 'product')
dfCamp2 = dfOriginal[bolCamp2]

orders = dfTrans.orderItems

lista = orders.iloc(0)[0:]

#Cria uma lista com o produto e o valor de venda, para alimentar um dataframe posteriormente
sum = 0
i = 0

listCateg = []

while i < len(lista):
    j = 0
    listaOrder = orders.iloc(0)[i]
    while j < len(listaOrder):
        sum = sum + (orders.iloc(0)[i][j]['price'] * orders.iloc(0)[i][j]['quantity'])
        prod = orders.iloc(0)[i][j]['product']
        linha = []
        linha.append(orders.iloc(0)[i][j]['product'])
        
        linha.append(orders.iloc(0)[i][j]['price'] * orders.iloc(0)[i][j]['quantity'])
        listCateg.append(linha)
        j = j + 1
    i = i + 1

dfTranProd = pd.DataFrame(listCateg, columns='product value'.split())

# Transforma o product para String na coluna productStr
dfCamp2['productStr'] = dfCamp2['product'].apply(strProduct)
dfTranProd['productStr'] = dfTranProd['product'].apply(strProduct)

# Agrupa por produto e categoria no df de produtos da campanha 2, deixando como um cadastro único de produtos
groupCamp2 = dfCamp2.groupby(['productStr','category'])
dfProdUnique = pd.DataFrame(groupCamp2.size().reset_index())

# Realiza uniã0 dos df de vendas e de produtos unicos
dfUnion = pd.merge(dfTranProd, dfProdUnique, on=['productStr'])

# Agrupa por categoria 
groupSum = dfUnion.groupby('category')

# cria o dataframe
dfSumCat = pd.DataFrame(groupSum['value'].sum().reset_index())

# Sort por ordem decrescente
dfSumCat.sort_values(by='value',ascending=False,inplace=True)

print(dfSumCat)

sns.barplot(x='category',y='value',data=dfSumCat.head())



# -- FUNÇÕES --

def returnCategory(prod):
    return dfCamp2[dfCamp2['product'] == prod]['category'].iloc(0)[0]

def strProduct(prod):
    return str(int(prod))
