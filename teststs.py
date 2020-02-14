import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

tips = px.data.()
df_train = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
col_options = [dict(label=x, value=x) for x in df_train.columns]
dimensions = ["x", "y", "color", "facet_col", "facet_row"]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Demo: Plotly Expressfdsfsafdsa in Dash with Tips Dataset"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", 
                                     "display": "inline-block"}
        ),
    ], className='ten columns', #style={'width':'80%', }
)

@app.callback(Output("graph", "figure"), 
              [Input(d, "value") for d in dimensions])
def make_figure(x, y, color, facet_col, facet_row):
    return px.scatter(
        tips,
        x=x,
        y=y,
        color=color,
        facet_col=facet_col,
        facet_row=facet_row,
        height=700,
    )

app.run_server(debug=True)
