import os
import pandas as pd
import psycopg2
import plotly.express as px
from dash import Dash, dcc, html

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
df = pd.read_sql("SELECT * FROM dados", conn)
conn.close()

fig = px.bar(df, x="nome", y="valor", title="Dados API")

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H2("Dashboard com Dados da API"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
