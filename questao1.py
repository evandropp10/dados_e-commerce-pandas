import numpy as np
import pandas as pd

dfOriginal = pd.read_json('ecommerce-events.ndjson', lines = True)

# Dataframe de transações
bolTran = dfOriginal.eventType == 'transaction'
dfTran = dfOriginal[bolTran]

# Series de orders (produto, quantidade, valor)
orders = dfTran.orderItems

lista = orders.iloc(0)[0:]

sum = 0
i = 0

# realiza a soma total
while i < len(lista):
    j = 0
    listaOrder = orders.iloc(0)[i]
    while j < len(listaOrder):
        sum = sum + (orders.iloc(0)[i][j]['price'] * orders.iloc(0)[i][j]['quantity'])
        j = j + 1
    i = i + 1

print(sum)