import pandas as pd
import plotly.graph_objects as go
import datetime as dt


def criando_grafico_acao(ticker):

    dados = pd.read_csv(r'dados\cotacoes.csv')
    dados['Date'] = pd.to_datetime(dados['Date'])
    dados = dados.set_index('Date')

    acao_grafico = dados[dados['Ticker'] == ticker]

    layout = go.Layout(yaxis=dict(tickfont=dict(color="#D3D6DF"), showline=False),
                       xaxis=dict(tickfont=dict(color="#D3D6DF"), showline=False))

    fig = go.Figure(data=[go.Candlestick(x=acao_grafico.index,
                                         open=acao_grafico['Open'],
                                         high=acao_grafico['High'],
                                         low=acao_grafico['Low'],
                                         close=acao_grafico['Close'])], layout=layout)

    fig.update_layout(margin=dict(l=24, r=45, t=31, b=23),
                      showlegend=False, font=dict(color="#D3D6DF"))

    fig.layout.plot_bgcolor = '#131516'
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)')

    fig.update_xaxes(tickcolor='#131516', showgrid=False)
    fig.update_yaxes(tickcolor='#131516', showgrid=False)

    fig.update_layout(xaxis_rangeslider_visible=False)

    return fig
