import dash_bootstrap_components as dbc
import dash
import pandas as pd
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output

app = dash.Dash(
    external_stylesheets=[dbc.themes.DARKLY]
)
