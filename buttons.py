

import dash_core_components as dcc
import dash_html_components as html

cat_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
                'PaperlessBilling', 'PhoneService', 'Contract', 'StreamingMovies',
                'StreamingTV', 'TechSupport', 'OnlineBackup', 'OnlineSecurity',
                'InternetService', 'MultipleLines', 'DeviceProtection', 'PaymentMethod']


def button_line():
    subtitle = html.Div(dcc.Markdown('''

**Churn rate**, when applied to a customer base, refers to the proportion of contractual customers or subscribers who leave a supplier during a given time period. It is a possible indicator of customer dissatisfaction, cheaper and/or better offers from the competition, more successful sales and/or marketing by the competition, or reasons having to do with the customer life cycle.\n\n

**Churn** is closely related to the concept of average customer life time. For example, an annual churn rate of 25 percent implies an average customer life of four years. An annual churn rate of 33 percent implies an average customer life of three years. The churn rate can be minimized by creating barriers which discourage customers to change suppliers (contractual binding periods, use of proprietary technology, value-added services, unique business models, etc.), or through retention activities such as loyalty programs. It is possible to overstate the churn rate, as when a consumer drops the service but then restarts it within the same year. Thus, a clear distinction needs to be made between "gross churn", the total number of absolute disconnections, and "net churn", the overall loss of subscribers or members. The difference between the two measures is the number of new subscribers or members that have joined during the same period. Suppliers may find that if they offer a loss-leader "introductory special", it can lead to a higher churn rate and subscriber abuse, as some subscribers will sign on, let the service lapse, then sign on again to take continuous advantage of current specials.\n\n

When talking about subscribers or customers, sometimes the expression "survival rate" is used to mean 1 minus the churn rate. For example, for a group of subscribers, an annual churn rate of 25 percent is the same as an annual survival rate of 75 percent. Both imply a customer lifetime of four years. I.e., a customer lifetime can be calculated as the inverse of that customer's predicted churn rate. For a group or segment of customers, their customer life (or tenure) is the inverse of their aggregate churn rate. Gompertz distribution models of distribution of customer life times can therefore also predict a distribution of churn rates.
'''),  className="row", style={'margin':'20px', 'padding-left':'35px'}
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
    ], className='three columns',
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
        style={'margin-top':'20px', 'display':'inline-block'}
    )

    return [subtitle, dropdown3, dropdown1, dropdown2, ]

def paragraphs():
    div = html.H1("Revenue Churn", style={'width':'85%', 'margin':'0 auto'})
    paragra = html.P(dcc.Markdown("**Revenue churn** is the monetary amount of recurring revenue lost in a period divided by the total revenue at the beginning of the period. Revenue churn is commonly used in Software as a Service (SaaS) and other business models that rely on recurring revenue models."), style={'width':'85%', 'margin':'0 auto'})

    return [div, paragra]
