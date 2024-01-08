from app import *
from components import grafico_ativo, noticias

app.layout = dbc.Container([

    dbc.Row([

        dbc.Col(grafico_ativo.layout_grafico, style={'margin-top': '200px'}),

        dbc.Col([

            dbc.Row([

                dbc.Col(),
                dbc.Col(html.H1(children='Notícias')),
                dbc.Col()

            ]),

            dbc.Row(noticias.layuot_noticias)

        ], style={'margin-top': '140px'})
    ])
], fluid=True, style={'height': '100vh', 'widht': '100%', 'padding': '25px 25px 0px'})


if __name__ == '__main__':

    app.run_server(debug=False, port=8052)
