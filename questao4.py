import numpy as np
import pandas as pd

dfOriginal = pd.read_json('ecommerce-events.ndjson', lines = True)

# Dataframe de Page
bolPage = dfOriginal.eventType == 'page'
dfPage = dfOriginal[bolPage]

# transforma coluna date para o formato datetime do pandas e grava na coluna dateTS
dfPage['dateTS'] = pd.to_datetime(dfPage['date'])

# dia da semana em inteiros
dfPage['weekDay'] = dfPage['dateTS'].apply(lambda time: time.dayofweek)

# converte o dia da semana para string
dayMap = {0:'Seg',1:'Ter',2:'Qua',3:'Qui',4:'Sex',5:'Sab',6:'Dom'}
dfPage['weekDay'] = dfPage['weekDay'].map(dayMap)

# Verifica qual tem mais acessos, o maior é segunda
dfPage['weekDay'].value_counts()

# coloca a hora de acesso na coluna hour
dfPage['hour'] = dfPage['dateTS'].apply(lambda time: time.hour)

# Classifica a hora em Madrugada, Manha, Tarde ou Noite
hourMap = {0:'Madrugada',1:'Madrugada',2:'Madrugada',3:'Madrugada',4:'Madrugada',5:'Madrugada',6:'Manha',7:'Manha',8:'Manha',9:'Manha',10:'Manha',11:'Manha',12:'Tarde',13:'Tarde',14:'Tarde',15:'Tarde',16:'Tarde',17:'Tarde',18:'Noite',19:'Noite',20:'Noite',21:'Noite',22:'Noite',23:'Noite'}
dfPage['dayPart'] = dfPage['hour'].map(hourMap)

# Verifica qual parte do dia tem mais acessos, é a tarde
dfPage['dayPart'].value_counts()

# Agrupa em dia da semana e parte do dia para verificar qual tem mais acessos, Segunda a noite
groupDay = dfPage.groupby(by=['weekDay','dayPart'])
groupDay['eventType'].count()