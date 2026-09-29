import pandas as pd
import yfinance as yf

# 1. Definimos el activo y el rango de fechas

simbolo = "^NDX"
fecha_inicio = "2025-09-01"
fecha_fin = "2026-09-01"

print(f"Descargando datos para {simbolo}...")

# 2. Descargar los datos desde Yahoo Finance
# Usamos el método .download() que nos devuelve directamente un DataFrame de Pandas
df = yf.download(simbolo, start=fecha_inicio, end=fecha_fin, interval="1d")
# 2.1 Eliminar multi-indice y aplanar el DataFrame
df.columns = df.columns.get_level_values(0)

# 3. Seleccionar solo la columna con los precios de cierre
df_close = df["Close"]

# 4. Crear nuevas columnas
# 4.1. Columna con el rango de moviento del dia
df["Range"] = df["High"]- df["Low"]
# 4.2. Columna con la variacion porcentual
df["Var"] = df["Close"].pct_change()*100
# 4.3 Mostrar las nuevas columnas

# 5 Eliminar los valores NaN
df = df.dropna()

print(df.tail())