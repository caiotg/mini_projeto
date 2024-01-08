from app import *
from funcao_grafico import criando_grafico_acao

lista_tickers = ['WEGE3', 'PETR4', 'CEAB3']

layout_grafico = [

    dbc.Row([

        dbc.Col(),
        dbc.Col(dcc.Dropdown(lista_tickers, value='PETR4', id='escolher-ticker',
                style={"background-color": 'black', 'color': 'white'})),
        dbc.Col()

    ]),

    dbc.Row(dcc.Graph(id='grafico_candle'))

]


@app.callback(
    Output('grafico_candle', 'figure'),
    Input('escolher-ticker', 'value')
)
def update_grafico_candle(ticker):

    fig = criando_grafico_acao(ticker)

    return fig
