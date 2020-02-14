# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output

# app = dash.Dash()

# app.layout = html.Div([
#     dcc.Input(id='my-id', value='Dash App', type='text'),
#     html.Div(id='my-div')
# ])


# @app.callback(
#     Output(component_id='my-div', component_property='children'),
#     [Input(component_id='my-id', component_property='value')]
# )
# def update_output_div(input_value):
#     return 'You\'ve entered "{}"'.format(input_value)


# if __name__ == '__main__':
#     app.run_server()

import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df_train = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)
server = app.server


app.layout = html.Div([
    html.Div([
        html.H2('Hello World'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in ['InternetService', 'MultipleLines', 
                                                        'DeviceProtection', 'PaymentMethod']],
            value='InternetService'
        ),
        dcc.Graph(id='display-value'),
        #html.Div(id='display-value'),
    ], className='three columns' )
])

## Using the decorator to receive inputs from the user
@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    print('You have selected "{}"'.format(value))
    print(df_train[value].head())
    data = go.Bar(
            x=df_train.groupby(value)['customerID'].count().index,
            y=df_train.groupby(value)['customerID'].count().values,
            marker=dict(
                color=['indianred', 'seagreen']),
        )
    return go.Figure(data=[data])


if __name__ == '__main__':
    app.run_server(debug=True)

