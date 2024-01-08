import pandas as pd
import yfinance as yf
import datetime as dt


def puxando_cotacoes():

    lista_acoes = ['PETR4.SA', 'WEGE3.SA', 'CEAB3.SA']

    hoje = dt.datetime.now()
    um_ano_atras = hoje - dt.timedelta(365)

    dados = yf.download(tickers=lista_acoes, start=um_ano_atras, end=hoje)[
        ['Open', 'High', 'Low', 'Close']]

    dados = dados.stack(level=1)
    dados = dados.reset_index()

    dados.columns = ['Date', 'Ticker', 'Close', 'High', 'Low', 'Open']
    dados['Ticker'] = dados['Ticker'].apply(lambda ticker: ticker[:-3])
    dados = dados.sort_values(by=['Ticker', 'Date'])

    dados.to_csv(fr'dados\cotacoes.csv', index=False)