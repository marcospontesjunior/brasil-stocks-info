import pandas as pd
import yfinance

lista_acoes = ["ITUB4.SA", "BBDC4.SA", "VALE3.SA", "PETR4.SA", "ABEV3.SA", "BBAS3.SA"]

acoes_info = []

for acoes in lista_acoes:
  acoes_info.append(yfinance.Ticker(acoes).history("1d"))

df = pd.concat(acoes_info, keys=lista_acoes, names=["Ação", "Data"])

df = df.drop(["Volume", "Dividends", "Stock Splits"], axis=1)

df = df.reorder_levels(["Data", "Ação"])

df.to_excel("dados_açoes_diaria.xlsx", index=False)