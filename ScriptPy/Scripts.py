import pandas as pd

x = pd.read_excel('libro.xlsx')
data = pd.DataFrame(columns=('departamento', 'municipio','puesto','partido','candidato'))

data.loc[0]=[x.groupby('departamento').size().keys().values,x.groupby('municipio').size().keys().values,x.groupby('nombre_puesto').size().keys().values,x.groupby('partido').size().keys().values,x.groupby('candidato').size().keys().values]
data.loc[1]=[x.groupby('departamento').size().values,x.groupby('municipio').size().values,x.groupby('nombre_puesto').size().values,x.groupby('partido').size().values,x.groupby('candidato').size().values]


data.to_csv('NewData.csv', sep=',')
