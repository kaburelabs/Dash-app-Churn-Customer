# Data Libraries
import pandas as pd
import numpy as np

# App libraries
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import dash.dependencies
import dash_auth
from dash.dependencies import Input, Output, State
# import requests


# Visualization Libraries
#import plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px


## THE COMPONENTS
## GRAPHS - LAYOUTS - BUTTONS
from graphsutils import plot_dist_churn, pie_norm, pie_churn, plot_dist_churn2
from layouts import graph_1, graph2_3, create_footer, create_header, header_logo, paragraphs
from buttons import button_line

## CSS EXTERNAL FILE
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 
                        'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
                        'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css']

## Some authentitications to test and login on app
# VALID_USERNAME_PASSWORD_PAIRS = {
#     'admin': 'admin',
#     'leo':'123456',
#     'test':'test'}

## Importing the dataset
df_train = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

## Some initial modification in the data
df_train['TotalCharges'].fillna(df_train['MonthlyCharges'], inplace=True)
df_train['Churn_label'] = df_train.Churn.copy()
df_train['Churn'] = df_train.Churn.replace({'Yes': 1, 'No': 0})
df_train['SeniorCitizen'] = df_train.SeniorCitizen.replace({0: 'No-Senior', 1:'Senior'})
df_train.loc[df_train['TotalCharges'] == ' ', 'TotalCharges'] = np.nan
df_train['TotalCharges'] = df_train['TotalCharges'].astype(float)

## App Name
app_name='Dashboard'

# Instantiating our app
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

# Seting the name to app
app.title=app_name

server = app.server

## Seting the authentication to the app with the pair passwords declared above 
# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )

# All functions inside a Div with a specific size
# It's all functions that I implemented on other python files
def tab_test1():
    tab1 = html.Div([
        html.Div(header_logo(), className='row', style={ 'text-align': 'center'}
        ), ## Title and logo inline
        #html.Div(paragraph_header(), className='row'),
        html.Div(button_line(), className='row', style={'background': '#bfd0f7', 'padding':'0px 24px', 'margin':'50px 0'}), # CheckBoxes e espaço, poderiam estar separados como os gráficos
        html.Div(graph_1(), className='row', style={'padding-top':'10'}), # first and principal graph
        html.Div(paragraphs(), className='row', style={'background': '#bfd0f7', 'padding':'0px 24px', 'margin':'24px 0'}), # Paragraph of explanation
        html.Div(graph2_3(), className='row') # Pie graphs
    ],className='container'# style={'width':'85%', 'margin':'0 auto'}
    ) # setting the class container to become all in a "box" on the browser. Only header and footer will be out of it
    return tab1

# main APP engine
app.layout = html.Div(children=[
    create_header(app_name), ## Header of the app
    tab_test1(), # Body of the APP
    html.Div(create_footer())], 
                              style={'overflow':'hidden'}
                              ) #create_footer()


###################################################
## first line of graphsGraph 1 of the first line ##
###################################################
@app.callback(
    dash.dependencies.Output('Graph1', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('churn-or-not', 'value')])
def binary_ploting_distributions(cat_col, binary_selected):
    from plotly import tools
    #print(binary_selected)
    if binary_selected == 'Churn':
        return plot_dist_churn(df_train, cat_col)
    else:
        return plot_dist_churn2(df_train, cat_col)

# 
@app.callback(
    dash.dependencies.Output('Graph3', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('dropdown2', 'value')])
def PieChart(val1, val2, limit=15):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    # count_trace = df_train[df_cat].value_counts()[:limit].to_frame().reset_index()
    return pie_churn(df_train, val1, val2, "No-Churn")

# 
@app.callback(
    dash.dependencies.Output('Graph5', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('dropdown2', 'value')])
def PieChart(val1, val2, limit=15):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    # count_trace = df_train[df_cat].value_counts()[:limit].to_frame().reset_index()
    return pie_churn(df_train, val1, val2, "Churn")

# 
@app.callback(
    dash.dependencies.Output('Graph2', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('dropdown2', 'value')])
def _graph_upgrade2(val1, val2):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    # count_trace = df_train[df_cat].value_counts()[:limit].to_frame().reset_index()
    return pie_norm(df_train, val1, val2)

# Graph of histogram in adressed on Graph4
@app.callback(
    dash.dependencies.Output('Graph4', 'figure'),
    [dash.dependencies.Input('dropdown2', 'value'),
     dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('churn-or-not', 'value')])
def _plotly_express(cat_col, color, churn):
    # tmp = df_train.groupby(color)[cat_col].sum().reset_index()
    # tmp = tmp.sort_values(color) 
    if churn == "Churn":
                fig = px.box(df_train, x=color, y=cat_col, #category_orders={color:df_train[color].value_counts},
                            color=df_train['Churn_label'], height=450, #legend=False,        
                            color_discrete_map={"Yes": "seagreen", 
                                                "No": "indianred"},
                            category_orders={str(color):df_train[color].value_counts().sort_index().index}
                            # opacity=.6,# height=400
                        )
                fig.update_layout(
                    title=f"Distribution of {cat_col} <br>by {color}",
                    xaxis_title=dict(), showlegend=False,
                    yaxis_title=f"{cat_col} Distribution", 
                    #width=560000,
                    title_x=.5, legend_title=f'Churn: ', 
                    xaxis={'type':'category'},
                    #legend_orientation='h', 
                    #legend=dict(y=-.06),
                    margin=dict(t=100, l=50)
                )
    else:
                fig = px.box(df_train, x=color, y=cat_col, 
                            height=450, #legend=False,        
                            category_orders={str(color):df_train[color].value_counts().sort_index().index},
                            color_discrete_sequence = ['seagreen'], 
                            # opacity=.6,# height=400
                    )

                fig.update_layout(
                    title=f"Distribution of {cat_col} <br>by {color}",
                    xaxis_title=dict(), showlegend=False,
                    yaxis_title=f"{cat_col} Distribution",

                    #width=560000,
                    title_x=.5, legend_title=f'Churn: ', 
                    xaxis={'type':'category'},
                    #legend_orientation='h', 
                    #legend=dict(y=-.06),
                    margin=dict(t=100, l=50)
                    )

    fig.update_xaxes(title='')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)





