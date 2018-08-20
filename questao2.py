import numpy as np
import pandas as pd

dfOriginal = pd.read_json('ecommerce-events.ndjson', lines = True)

# Dataframe de Page
bolPage = dfOriginal.eventType == 'page'
dfPage = dfOriginal[bolPage]

# guarda em variável o total de devices
total = dfPage.deviceType.count()

# agrua por device
groupDevice = dfPage.groupby('deviceType')

# total de mobile
totalMobile = groupDevice.deviceType.count()[1]

# percentual de mobile
perMobile = totalMobile * 100 / total

print(perMobile)