#questão 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vendas.csv')

print(df.head())
print(df.shape)
df.info()

#questão 2
print(df.describe())
print(df['preco'].describe())

#questão 3
precos = np.array(df['preco'])

print("Média:", np.mean(precos))
print("Máximo:", np.max(precos))
print("Mínimo:", np.min(precos))
print("Tamanho:", precos.size)

#questão 4
print(df.isnull().sum())

df['preco'] = df['preco'].fillna(df['preco'].median())

#questão 5
print("Duplicados:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicados restantes:", df.duplicated().sum())

#questão 6
df['total'] = df['preco'] * df['quantidade']

print(df.head())

#questâo 7
filtro = df[(df['regiao'] == 'Sul') & (df['quantidade'] > 5)]

print(filtro)

#questão 8
resumo = df.groupby('categoria').agg({
    'preco': 'mean',
    'quantidade': 'sum',
    'total': 'sum'
})

print(resumo)

#questão 9
df.groupby('categoria')['total'].sum().plot(kind='bar')

plt.title('Total de vendas por categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor total das vendas')
plt.show()