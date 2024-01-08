from app import *

layuot_noticias = [

    html.Div(id='noticias-empresa')

]


def gerar_tabela_noticias(noticias):

    layout = [dbc.Col([

        dbc.Row([

            html.A(children=[

                html.P(
                    children=noticias['subtopico'].iloc[0], className='h3-noticias'),
                html.H3(
                    children=noticias['manchete'].iloc[0], className='manchete')

            ], href=noticias['link'].iloc[0], target='_blank', className='links-noticias')
        ], style={'margin-top': '16px'}),
        dbc.Row([

            html.A(children=[

                html.P(
                    children=noticias['subtopico'].iloc[1], className='h3-noticias'),
                html.H3(
                    children=noticias['manchete'].iloc[1], className='manchete')

            ], href=noticias['link'].iloc[1], target='_blank', className='links-noticias')

        ], style={'margin-top': '24px'}),
        dbc.Row([

            html.A(children=[

                html.P(
                    children=noticias['subtopico'].iloc[2], className='h3-noticias'),
                html.H3(
                    children=noticias['manchete'].iloc[2], className='manchete')

            ], href=noticias['link'].iloc[2], target='_blank', className='links-noticias')
        ], style={'margin-top': '24px'})
    ])]

    return layout


@app.callback(
    Output('noticias-empresa', 'children'),
    Input('escolher-ticker', 'value')

)
def update_tabela_noticias(ticker):

    noticias = pd.read_csv(r'dados\noticias.csv')
    noticias = noticias[noticias['ticker'] == ticker]

    layout_tabela = gerar_tabela_noticias(noticias)

    return layout_tabela
