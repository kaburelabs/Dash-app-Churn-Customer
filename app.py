# Data Libraries
import pandas as pd
import numpy as np

# App libraries
from dash import dcc, html, Input, Output, State, Dash

# from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# Visualization Libraries
# import plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px

from components.Navbar import navbar

# THE COMPONENTS
## GRAPHS - LAYOUTS - BUTTONS
from components.graphsutils import (
    plot_dist_churn,
    pie_norm,
    pie_churn,
    plot_dist_churn2,
)
from components.layouts import graph_1, graph2_3, create_footer, header_logo, paragraphs
from components.buttons import button_line

# Importing the dataset
df_train = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Some initial modification in the data
df_train["TotalCharges"].fillna(df_train["MonthlyCharges"], inplace=True)
df_train["Churn_label"] = df_train.Churn.copy()
df_train["Churn"] = df_train.Churn.replace({"Yes": 1, "No": 0})
df_train["SeniorCitizen"] = df_train.SeniorCitizen.replace(
    {0: "No-Senior", 1: "Senior"}
)
df_train.loc[df_train["TotalCharges"] == " ", "TotalCharges"] = np.nan
df_train["TotalCharges"] = df_train["TotalCharges"].astype(float)

# App Name
app_name = "Churn Customer Dashboard"

external_stylesheets = [
    dbc.themes.BOOTSTRAP,  # adding the bootstrap inside the application
    "https://use.fontawesome.com/releases/v5.8.1/css/all.css",
]

# Instantiating our app
app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1",
        },
    ],
)

# Seting the name to app
app.title = app_name

server = app.server

# All functions inside a Div with a specific size
# It's all functions that I implemented on other python files

def tab_test1():
    tab1 = dbc.Container(
        [
            #         ),  # Title and logo inline
            dbc.Row(
                header_logo(),
                className="textBackground padding40 bottom32 top32 margin-auto radius8",  # style={'margin': '24px 0', 'padding': '24px 24px 10px 24px'}
            ),  # Title and logo inline
            # html.Div(paragraph_header(), className='row'),
            # CheckBoxes e espaço, poderiam estar separados como os gráficos
            html.Div(
                button_line(),
                # className='row', style={
                #          'background': '#f77754', 'padding': '0px 24px', 'margin': '24px 0'}
            ),
            dbc.Row(graph_1()),  # first and principal graph
            # Paragraph of explanation
            dbc.Row(
                paragraphs(),
                className="textBackground padding40 bottom32 top32 margin-auto",
            ),
            html.Div(graph2_3()),  # Pie graphs
        ],  # style={"maxWidth": "960px"}
    )  # setting the class container to become all in a "box" on the browser. Only header and footer will be out of it
    return tab1


# main APP engine
app.layout = html.Div(
    children=[
        navbar,  # Header of the app
        tab_test1(),  # Body of the APP
        html.Div(create_footer()),
    ],
    style={"overflow": "hidden"},
)  # create_footer()


###################################################
## first line of graphsGraph 1 of the first line ##
###################################################
@app.callback(
    Output("Graph1", "figure"),
    [
        Input("dropdown", "value"),
        Input("churn-or-not", "value"),
    ],
)
def binary_ploting_distributions(cat_col, binary_selected):

    # print(binary_selected)
    if binary_selected == "Churn":
        return plot_dist_churn(df_train, cat_col)
    else:
        return plot_dist_churn2(df_train, cat_col)

@app.callback(
    Output("Graph3", "figure"),
    [
        Input("dropdown", "value"),
        Input("dropdown2", "value"),
    ],
)
def PieChart(val1, val2, limit=15):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    # count_trace = df_train[df_cat].value_counts()[:limit].to_frame().reset_index()
    return pie_churn(df_train, val1, val2, "No-Churn")


#


@app.callback(
    Output("Graph5", "figure"),
    [
        Input("dropdown", "value"),
        Input("dropdown2", "value"),
    ],
)
def PieChart(val1, val2, limit=15):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    # count_trace = df_train[df_cat].value_counts()[:limit].to_frame().reset_index()
    return pie_churn(df_train, val1, val2, "Churn")


#


@app.callback(
    Output("Graph2", "figure"),
    [
        Input("dropdown", "value"),
        Input("dropdown2", "value"),
    ],
)
def _graph_upgrade2(val1, val2):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    # count_trace = df_train[df_cat].value_counts()[:limit].to_frame().reset_index()
    return pie_norm(df_train, val1, val2)


# Graph of histogram in adressed on Graph4


@app.callback(
    Output("Graph4", "figure"),
    [
        Input("dropdown2", "value"),
        Input("dropdown", "value"),
        Input("churn-or-not", "value"),
    ],
)
def _plotly_express(cat_col, color, churn):
    # tmp = df_train.groupby(color)[cat_col].sum().reset_index()
    # tmp = tmp.sort_values(color)
    if churn == "Churn":
        fig = px.box(
            df_train,
            x=color,
            y=cat_col,  # category_orders={color:df_train[color].value_counts},
            # legend=False,
            color=df_train["Churn_label"].map({"Yes": "Churn", "No": "NoChurn"}),
            height=450,
            color_discrete_map={"Churn": "seagreen", "NoChurn": "indianred"},
            category_orders={
                str(color): df_train[color].value_counts().sort_index().index
            }
            # opacity=.6,# height=400
        )
        fig.update_layout(
            title=f"{cat_col} dist by <br>{color} & Churn",
            xaxis_title=dict(),
            showlegend=True,
            yaxis_title=f"{cat_col} Distribution",
            title_x=0.5,
            legend_title=f"Churn:",
            xaxis={"type": "category"},
            # legend_orientation='h',
            # legend=dict(y=-.06),
            margin=dict(t=100, l=50),
        )
    else:
        fig = px.box(
            df_train,
            x=color,
            y=cat_col,
            height=450,  # legend=False,
            category_orders={
                str(color): df_train[color].value_counts().sort_index().index
            },
            color_discrete_sequence=["seagreen"]
            # opacity=.6,# height=400
        )

        fig.update_layout(
            title=f"Distribution of {cat_col} <br>by {color}",
            xaxis_title=dict(),
            showlegend=False,
            yaxis_title=f"{cat_col} Distribution",
            # width=560000,
            title_x=0.5,
            legend_title=f"Churn:",
            xaxis={"type": "category"},
            # legend_orientation='h',
            # legend=dict(y=-.06),
            margin=dict(t=100, l=50),
        )

    fig.update_xaxes(title="")

    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=4445)
