import pandas as pd

print("Cargando datos...")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df = pd.read_csv(url)

print("Datos cargados ✅")

print(df.head())
print(df.info())

print("\nConteo de sobrevivientes:")
print(df["survived"].value_counts())



print("\nSobrevivientes:")
print(df["survived"].value_counts())
conteo = df["survived"].value_counts()

print("\nResultados:")
print(f"No sobrevivieron: {conteo[0]}")
print(f"Sí sobrevivieron: {conteo[1]}")
print("\nSobrevivencia por género:")
print(df.groupby("sex")["survived"].mean())

total = len(df)
sobrevivieron = df["survived"].sum()
murieron = total - sobrevivieron

print("\nResumen:")
print(f"Total de pasajeros: {total}")
print(f"Sobrevivieron: {sobrevivieron}")
print(f"No sobrevivieron: {murieron}")

print("\nSobrevivencia por género:")
print(df.groupby("sex")["survived"].mean())
