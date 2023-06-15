

from dash import dcc, html
import dash_bootstrap_components as dbc

cat_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
                'PaperlessBilling', 'PhoneService', 'Contract', 'StreamingMovies',
                'StreamingTV', 'TechSupport', 'OnlineBackup', 'OnlineSecurity',
                'InternetService', 'MultipleLines', 'DeviceProtection', 'PaymentMethod']


def button_line():

    dropdown1 = dbc.Col(html.Div(
        [
            html.Div("Categorical Features: ", className="bold font-sm"),
            dcc.Dropdown(
                id='dropdown',
                options=[{'label': i, 'value': i} for i in cat_features],
                value='DeviceProtection',
            ),
        ],
        className="displayColor padding16 radius8"),
        width={"size": 10, "offset": 1},
        md={"size": 6, "offset": 0},
        lg={"size": 4, "offset": 0},
        className="bottom16"
    )

    dropdown2 = dbc.Col(html.Div(
        [
            html.Div("Numerical Features: ", className="bold font-xs"),
            dcc.Dropdown(
                id='dropdown2',
                options=[{'label': 'MonthlyCharges', 'value': 'MonthlyCharges'},
                         {'label': 'TotalCharges', 'value': 'TotalCharges'}],
                value='MonthlyCharges',
            ),
        ],
        className="displayColor padding16 radius8"),
        width={"size": 10, "offset": 1},
        md={"size": 6, "offset": 0},
        lg={"size": 4, "offset": 0},
        className="bottom16"
    )

    radiobutton = dbc.Col(html.Div(
        [
            html.Div("Distribution Form: ", className="bold font-sm"),
            dcc.RadioItems(
                id='churn-or-not',
                options=[{'label': 'Churn', 'value': 'Churn'},
                         {'label': 'General', 'value': 'Normal'},
                         # 'padding-right':'16px'
                         ], labelStyle={'display': 'inline-block', "margin": "auto 15px"
                                        },
                value='Churn',  style={'margin': '6px 0'}
            ),
        ],
        className="displayColor padding16 radius8"),
        width={"size": 10, "offset": 1},
        md={"size": 6, "offset": 3},
        lg={"size": 4, "offset": 0},
        className="bottom16")

    return dbc.Row([radiobutton, dropdown1, dropdown2])
