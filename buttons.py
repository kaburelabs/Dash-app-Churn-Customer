

import dash_core_components as dcc
import dash_html_components as html

cat_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
                'PaperlessBilling', 'PhoneService', 'Contract', 'StreamingMovies',
                'StreamingTV', 'TechSupport', 'OnlineBackup', 'OnlineSecurity',
                'InternetService', 'MultipleLines', 'DeviceProtection', 'PaymentMethod']


def button_line():
    subtitle = html.Div(children='Predict behavior to retain customers.<br> You can analyze all relevant customer data and develop focused customer retention programs. [IBM Sample Data Sets]',
                        className="six columns", style={'margin':'20px', 'padding-left':'35px'}
                        )
    dropdown1 = html.Div(
        [
        html.P("Categorical Features: "),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in cat_features],
            value='DeviceProtection',
        ),
    ], className='two columns',
        style={'margin':'20px', 'display':'inline-block'})
    dropdown2 = html.Div(
        [
        html.P("Numerical Features: "),
        dcc.Dropdown(
            id='dropdown2',
            options=[{'label': 'MonthlyCharges', 'value': 'MonthlyCharges'},
                     {'label': 'TotalCharges', 'value':'TotalCharges'}] ,
            value='MonthlyCharges',
        ),
    ], className='two columns',
        style={'margin':'20px', 'display':'inline-block'}
    )
    dropdown3 = html.Div(
        [
        html.P("Distribution Form: "),
        dcc.RadioItems(
            id='churn-or-not',
            options=[{'label': 'General', 'value': 'Normal'},
                     {'label': 'Churn', 'value':'Churn'}] ,
            value='Normal',
        ),
    ], className='two columns',
        style={'margin-top':'20px', 'display':'inline-block', 'padding-left':'60px'}
    )

    return [dropdown3, dropdown1, dropdown2, subtitle]

def paragraphs():
    div = html.H1("Ternure")
    paragra = html.P("Blablablabla lbalbalba balbalbalbla balbalbalBlablablabla \
                     lbalbalba balbalbalbla balbalbalBlablablabla lbalbalba\
                     balbalbalbla balbalbalBlablablabla lbalbalba balbalbalbla\
                     balbalbalBlablablabla lbalbalba balbalbalbla balbalbalBlablablabla\
                     lbalbalba balbalbalbla balbalbalBlablablabla lbalbalba balbalbalbla \
                     balbalbalBlablablabla lbalbalba balbalbalbla balbalbal")

    return [div, paragra]
