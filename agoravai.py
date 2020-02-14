import pandas as pd

# Import Dash Visualization Libraries
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import dash.dependencies
from dash.dependencies import Input, Output, State
import plotly
from scipy import stats

import plotly.graph_objs as go
import plotly.tools as tls

from plotly.offline import iplot, init_notebook_mode
#import cufflinks
#import cufflinks as cf
import plotly.figure_factory as ff



df_train = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')



app = dash.Dash()


app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

colors = {
    'background': '#111111',
    'text': '#7f7f7f'
}

cat_features = [ 'gender', 'SeniorCitizen', 'Partner',
                 'Dependents', 'PaperlessBilling', 'PhoneService', 
                 'Contract', 'StreamingMovies', 'StreamingTV', 
                 'TechSupport', 'OnlineBackup', 'OnlineSecurity',
                 'InternetService', 'MultipleLines', 'DeviceProtection', 
                 'PaymentMethod']

app.layout = html.Div(
                html.Div([
                  style={'backgroundColor': colors['background']},
                  children=[
                            html.H1(
                                    children='Hello Dash',
                                            style={
                                                    'textAlign': 'center',
                                                    'color': colors['text'],
                                                    #"height" : "25%", "width" : "10%"
                                                }
                            ),
                            
                html.Div(children='Dash: A web application framework for Python.', 
                        style={'textAlign': 'center',
                                'color': colors['text']}),
                    html.Div([
                                dcc.Graph(
                                    id='Graph1',
                                    figure={'data':[trace0], 'layout':layout}, 
                                ),
                                dcc.Graph(
                                    id='Graph2',
                                    figure={'data':[trace1], 'layout':layout2}, 
                                )
                            ],
                        ], className="six columns")))


trace0 = go.Bar(
    x=df_train.groupby('Churn')['customerID'].count().index,
    y=df_train.groupby('Churn')['customerID'].count().values,
    marker=dict(
        color=['indianred', 'seagreen']),
)
trace1 = go.Bar(
    x=df_train.groupby('PhoneService')['customerID'].count().index,
    y=df_train.groupby('PhoneService')['customerID'].count().values,
    marker=dict(
        color=['indianred', 'seagreen']),
)
data = [trace0]

layout = go.Layout(
    title='Churn (Target) Distribution', 
    titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7f7f7f'
        ),
    xaxis=dict(
        title='Customer Churn?', titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7f7f7f'
        )),
    yaxis=dict(
        title='Count', titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7f7f7f'
        )), 
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font=dict(color=colors['text'],
    #margin=dict(l=50, r=2,t=40, b=1)
    )      
)

layout2 = go.Layout(
    title='Churn (Target) Di22stribution', 
    titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7f7f7f'
        ),
    xaxis=dict(
        title='Customer Churn?', titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7f7f7f'
        )),
    yaxis=dict(
        title='Count', titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7f7f7f'
        )), 
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font=dict(color=colors['text'],
    #margin=dict(l=50, r=2,t=40, b=1)
    )      
)

if __name__ == '__main__':
    app.run_server(debug=False)