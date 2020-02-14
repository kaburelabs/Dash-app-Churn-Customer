# Data Libraries
import pandas as pd
import numpy as np

# App libraries
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import dash.dependencies
import dash_auth
import requests
from dash.dependencies import Input, Output, State

# Visualization Libraries
import plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from plotly.offline import iplot, init_notebook_mode
import plotly.express as px
import plotly
from plotly.offline import iplot

# LIBRARIES WHERE I SET ALL THE COMPONENTS
## GRAPHS - LAYOUTS - BUTTONS
from graphsutils import plot_dist_churn, pie_norm, pie_churn
from layouts import graph_1, graph2_3, create_footer, create_header, header_logo
from buttons import button_line, paragraphs

## CSS EXTERNAL FILE
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

## Some authentitications to test and login on app
VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world',
    'admin': 'admin',
    'leo':'123456',
    'teste':'teste'}

## Importing the dataset
df_train = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

## Some initial modification in the data
df_train['TotalCharges'].fillna(df_train['MonthlyCharges'], inplace=True)
df_train['Churn'] = df_train.Churn.replace({'Yes': 1, 'No': 0})
df_train.loc[df_train['TotalCharges'] == ' ', 'TotalCharges'] = np.nan
df_train['TotalCharges'] = df_train['TotalCharges'].astype(float)


## App Name
app_name='Dashboard'

# Instantiating our app
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

# Seting the name to app
app.title=app_name

## Seting the authentication to the app with the pair passwords declared above 
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

# All functions inside a Div with a specific size
# It's all functions that I implemented on other python files
def tab_test1():
    tab1 = html.Div([
        html.Div(header_logo(), className='row', style={'width': '100%', 'text-align': 'center'}), ## Title and logo inline
        html.Div(button_line(), className='row', ), # CheckBoxes e espaço, poderiam estar separados como os gráficos
        html.Div(graph_1(), className='row', style={'padding-top':'10'}), # first and principal graph
        html.Div(paragraphs(), className='row',), # Paragraph of explanation
        html.Div(graph2_3(), className='row') # Pie graphs
    ], style={'width':'85%', 'margin':'0 auto'}) # setting the class container to become all in a "box" on the browser. Only header and footer will be out of it
    return tab1


# main APP engine
app.layout = html.Div(children=[
    create_header(app_name), ## Header of the app
    tab_test1(), # Body of the APP
    html.Div(create_footer(), className='twelve columns')], style={'overflow':'hidden'}) #create_footer()


# Graph of histogram in adressed on Graph4
@app.callback(
    dash.dependencies.Output('Graph4', 'figure'),
    [dash.dependencies.Input('dropdown2', 'value'),
     dash.dependencies.Input('dropdown', 'value'),])
def plotly_express_test(cat_col, color):
    fig = px.histogram(df_train, x=cat_col, color=color,# height=500
    ) 
    fig.update_layout(
        title=f"Distribution of {cat_col} <br>by {color}",
        xaxis_title="Value Range Distribution",
        yaxis_title=f"{cat_col} Distribution", height=500,
        title_x=.5, legend_orientation='h', 
                    legend=dict(x=.08, y=.999)
    )

    return fig


###################################################
## first line of graphsGraph 1 of the first line ##
###################################################
@app.callback(
    dash.dependencies.Output('Graph1', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])
def binary_ploting_distributions(cat_col):
    from plotly import tools
    #teseeete = teste1(1, 5)
    #print(f'tetestestsetsetsetestse: {teseeete}')
    return plot_dist_churn(df_train, cat_col)


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


if __name__ == '__main__':
    app.run_server(debug=True)

