

import dash_core_components as dcc
import dash_html_components as html

cat_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
                'PaperlessBilling', 'PhoneService', 'Contract', 'StreamingMovies',
                'StreamingTV', 'TechSupport', 'OnlineBackup', 'OnlineSecurity',
                'InternetService', 'MultipleLines', 'DeviceProtection', 'PaymentMethod']


def button_line():

    dropdown1 = html.Div(
        [
        html.P("Categorical Features: ", style={'font-weight':'bold'}),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in cat_features],
            value='DeviceProtection',
        ),
    ], className='three columns',
        style={'margin':'20px', 'display':'inline-block'})

    dropdown2 = html.Div(
        [
        html.P("Numerical Features: ", style={'font-weight':'bold'}),
        dcc.Dropdown(
            id='dropdown2',
            options=[{'label': 'MonthlyCharges', 'value': 'MonthlyCharges'},
                     {'label': 'TotalCharges', 'value':'TotalCharges'}] ,
            value='MonthlyCharges',
        ),
    ], className='three columns',
        style={'margin':'20px', 'display':'inline-block'}
    )
    dropdown3 = html.Div(
        [
        html.P("Distribution Form: ", style={'font-weight':'bold'}),
        dcc.RadioItems(
            id='churn-or-not',
            options=[{'label': 'Churn', 'value':'Churn'}, 
                     {'label': 'General', 'value': 'Normal'},
                     ], labelStyle={'display':'inline-block', 'padding-right':'16px'} ,
            value='Churn', #style={'display':'inline-block'}
        ), 
    ], className='three columns', style={'margin-top':'20px', 'display':'inline-block'}
    )

    return [dropdown3, dropdown1, dropdown2, ]

def paragraphs():
    div = html.H1("Revenue Churn", style={'width':'85%', 'margin':'0 auto'})
    paragra = html.P(dcc.Markdown("**Revenue churn** is the monetary amount of recurring revenue lost in a period divided by the total revenue at the beginning of the period. Revenue churn is commonly used in Software as a Service (SaaS) and other business models that rely on recurring revenue models."), style={'width':'85%', 'margin':'0 auto'})

    return [div, paragra]


