

import dash_core_components as dcc
import dash_html_components as html

cat_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
                'PaperlessBilling', 'PhoneService', 'Contract', 'StreamingMovies',
                'StreamingTV', 'TechSupport', 'OnlineBackup', 'OnlineSecurity',
                'InternetService', 'MultipleLines', 'DeviceProtection', 'PaymentMethod']


def button_line():
    subtitle = html.Div(children='''<b>Predict behavior to retain customers.<b>\n You can analyze all relevant customer data and develop focused customer retention programs. [IBM Sample Data Sets] ''',
                        className="six columns", #style={'border-style': 'dotted'}
                        )
    dropdown1 = html.Div(
        [
        html.P("Categorical Features: "),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in cat_features],
            value='DeviceProtection',
        ),
    ], className='three columns',
        style={'margin-top': '10', 'margin-bottom':'20'})
    dropdown2 = html.Div(
        [
        html.P("Numerical Features: "),
        dcc.Dropdown(
            id='dropdown2',
            options=[{'label': 'MonthlyCharges', 'value': 'MonthlyCharges'},
                     {'label': 'TotalCharges', 'value':'TotalCharges'}] ,
            value='MonthlyCharges',
        ),
    ], className='three columns',
        style={'margin-top': '50', 'margin-bottom':'20', 'display':'inline-block'}
    )
    
    return [subtitle, dropdown1, dropdown2]

def paragraphs():
    div = html.H1("Ternure")
    paragra = html.P("Blablablabla lbalbalba balbalbalbla balbalbalBlablablabla \
                     lbalbalba balbalbalbla balbalbalBlablablabla lbalbalba\
                     balbalbalbla balbalbalBlablablabla lbalbalba balbalbalbla\
                     balbalbalBlablablabla lbalbalba balbalbalbla balbalbalBlablablabla\
                     lbalbalba balbalbalbla balbalbalBlablablabla lbalbalba balbalbalbla \
                     balbalbalBlablablabla lbalbalba balbalbalbla balbalbal")

    return [div, paragra]
