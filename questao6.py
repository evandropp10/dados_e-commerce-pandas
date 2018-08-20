import numpy as np
import pandas as pd

dfOriginal = pd.read_json('ecommerce-events.ndjson', lines = True)

bolProd = (dfOriginal.eventType == 'product')
dfProd = dfOriginal[bolProd]

disp = dfProd['status'].value_counts()[0]
indisp = dfProd['status'].value_counts()[1]
total = disp + indisp

# Fórmula da variancia
varQuant = (total - disp) / disp

print(varQuant)