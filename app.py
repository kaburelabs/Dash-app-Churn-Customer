# Upwork 19/05/20
# Viewd 59.0935%
# Interviewed 35.4213%
# Hired 34.3664%
# ____________________

# Upwork 20/05/20
# Viewd 58.2589%
# Interviewed 35.4012%
# Hired 33.6856%
# ____________________

# Upwork 20/05/20
# Viewd 58.2589%
# Interviewed 35.4012%
# Hired 33.6856%
# ____________________


# Data Libraries
import pandas as pd
import numpy as np

# App libraries
import dash_core_components as dcc
import dash_html_components as html

import dash.dependencies
import dash_auth
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_trich_components as dtc
# import requests

# Visualization Libraries
#import plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px


# THE COMPONENTS
## GRAPHS - LAYOUTS - BUTTONS
from graphsutils import plot_dist_churn, pie_norm, pie_churn, plot_dist_churn2
from layouts import graph_1, graph2_3, create_footer, header_logo, paragraphs
from buttons import button_line

# CSS EXTERNAL FILE
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
                        'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css']

# Some authentitications to test and login on app
# VALID_USERNAME_PASSWORD_PAIRS = {
#     'admin': 'admin',
#     'leo':'123456',
#     'test':'test'}

# Importing the dataset
df_train = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Some initial modification in the data
df_train['TotalCharges'].fillna(df_train['MonthlyCharges'], inplace=True)
df_train['Churn_label'] = df_train.Churn.copy()
df_train['Churn'] = df_train.Churn.replace({'Yes': 1, 'No': 0})
df_train['SeniorCitizen'] = df_train.SeniorCitizen.replace(
    {0: 'No-Senior', 1: 'Senior'})
df_train.loc[df_train['TotalCharges'] == ' ', 'TotalCharges'] = np.nan
df_train['TotalCharges'] = df_train['TotalCharges'].astype(float)

# App Name
app_name = 'Churn Customer Dashboard'

# Instantiating our app
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                meta_tags=[

                    {

                        "name": "viewport",

                        "content": "width=device-width, initial-scale=1, maximum-scale=1",

                    },

                ],)

# Seting the name to app
app.title = app_name

server = app.server

# Seting the authentication to the app with the pair passwords declared above
# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )

# All functions inside a Div with a specific size
# It's all functions that I implemented on other python files


def navbar(logo="/assets/logo-placeholder.png", height="35px",  appname="PlaceHolder Name"):

    navbar = html.Div(
        [dbc.Container(
            [dbc.Row([
                dbc.Col(html.A(
                    # Use row and col to control vertical alignment of logo / brand


                        html.Div(
                            "trich.ai", className="trich-navbar white font-xl", ),


                        # align="center",
                        # no_gutters=True,

                        href="https://trich.ai",
                        ), width=4),
                dbc.Col(dbc.NavbarBrand(
                    appname, className="font-md text-white"), className="text-right", width=8)],
                style={"align-items": "center", "min-height": "75px"}
            )
            ],
            style={"maxWidth": "1140px"})
         ],  # color="#393939",
        className="bottom32 navbarColor",
        # style={'height': '100px', "borderBottom":".5px solid lightgrey", "padding":"18px 0px"}

        # dark=True,
    )

    return navbar


def tab_test1():
    tab1 = dbc.Container([
        # dbc.Row(header_logo(), className="text-center colorSecondary", style={'text-align': 'center', 'background': '#a4d1c8',
        #                                                                       'margin': '24px 0', 'padding': '24px 24px 10px 24px'}

        #         ),  # Title and logo inline
        dbc.Row(header_logo(), className="textBackground padding40 bottom32 top32 margin-auto",  # style={'margin': '24px 0', 'padding': '24px 24px 10px 24px'}
                ),  # Title and logo inline
        #html.Div(paragraph_header(), className='row'),
        # CheckBoxes e espaço, poderiam estar separados como os gráficos
        html.Div(button_line(),
                 # className='row', style={
                 #          'background': '#f77754', 'padding': '0px 24px', 'margin': '24px 0'}
                 ),
        dbc.Row(graph_1()),  # first and principal graph
        # Paragraph of explanation
        dbc.Row(paragraphs(),
                className="textBackground padding40 bottom32 top32 margin-auto"),
        html.Div(graph2_3())  # Pie graphs
    ], style={"maxWidth": "1140px"}
    )      # setting the class container to become all in a "box" on the browser. Only header and footer will be out of it
    return tab1


# main APP engine
app.layout = html.Div(children=[
    navbar(appname=app_name),  # Header of the app
    tab_test1(),  # Body of the APP
    html.Div(create_footer())],
    style={'overflow': 'hidden'}
)  # create_footer()


###################################################
## first line of graphsGraph 1 of the first line ##
###################################################
@app.callback(
    dash.dependencies.Output('Graph1', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('churn-or-not', 'value')])
def binary_ploting_distributions(cat_col, binary_selected):
    from plotly import tools
    # print(binary_selected)
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
        fig = px.box(df_train, x=color, y=cat_col,  # category_orders={color:df_train[color].value_counts},
                     # legend=False,
                     color=df_train['Churn_label'].map({'Yes': 'Churn', 'No': 'NoChurn'}), height=450,
                     color_discrete_map={"Churn": "seagreen",
                                         "NoChurn": "indianred"},
                     category_orders={
                         str(color): df_train[color].value_counts().sort_index().index}
                     # opacity=.6,# height=400
                     )
        fig.update_layout(
            title=f"{cat_col} dist by <br>{color} & Churn",
            xaxis_title=dict(), showlegend=True,
            yaxis_title=f"{cat_col} Distribution",
            title_x=.5, legend_title=f'Churn:',
            xaxis={'type': 'category'},
            # legend_orientation='h',
            # legend=dict(y=-.06),
            margin=dict(t=100, l=50)
        )
    else:
        fig = px.box(df_train, x=color, y=cat_col,
                     height=450,  # legend=False,
                     category_orders={
                         str(color): df_train[color].value_counts().sort_index().index},
                     color_discrete_sequence=['seagreen']
                     # opacity=.6,# height=400
                     )

        fig.update_layout(
            title=f"Distribution of {cat_col} <br>by {color}",
            xaxis_title=dict(), showlegend=False,
            yaxis_title=f"{cat_col} Distribution",

            # width=560000,
            title_x=.5, legend_title=f'Churn:',
            xaxis={'type': 'category'},
            # legend_orientation='h',
            # legend=dict(y=-.06),
            margin=dict(t=100, l=50)
        )

    fig.update_xaxes(title='')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=4445)
