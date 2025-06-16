import pandas as pd

df = pd.read_csv('../dados/diabetes_simulado.csv')
df.fillna(df.mean(numeric_only=True), inplace=True)
df.to_csv('../dados/diabetes_limpo.csv', index=False)
