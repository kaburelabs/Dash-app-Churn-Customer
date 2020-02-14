import pandas as pd

# Import Dash Visualization Libraries
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import dash.dependencies
import dash_auth
import requests
from dash.dependencies import Input, Output, State
from plotly.offline import iplot
import numpy as np
# Standard plotly imports
import plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from plotly.offline import iplot, init_notebook_mode
import plotly.express as px
import plotly

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Boostrap CSS.

VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world',
    'admin': 'admin',
    'leo':'123test',
    'natacha':'4747'
}

app_name='trich.ai | Dashboard'
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)
app.title=app_name

df_train = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
df_train['TotalCharges'].fillna(df_train['MonthlyCharges'], inplace=True)
df_train['Churn'] = df_train.Churn.replace({'Yes': 1, 'No': 0})
df_train.loc[df_train['TotalCharges'] == ' ', 'TotalCharges'] = np.nan
df_train['TotalCharges'] = df_train['TotalCharges'].astype(float)


auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)


cat_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
                'PaperlessBilling', 'PhoneService', 'Contract', 'StreamingMovies',
                'StreamingTV', 'TechSupport', 'OnlineBackup', 'OnlineSecurity',
                'InternetService', 'MultipleLines', 'DeviceProtection', 'PaymentMethod']


trich_branco = "https://scontent.fcgh5-1.fna.fbcdn.net/v/t1.15752-9/58691848_279354386280172_5205780501993881600_n.png?_nc_cat=108&_nc_eui2=AeFD5xvGsjPVP35u6guRIh6RE0oRcdeykl_ofWB-ZhAJOqIzqCfcnlOyFLI9p6QKopkaqa355fiRGMa5mLPNDCxz_cWugXY5-VxtSQ7rpltCHg&_nc_ohc=eLFFs8xpOLkAX_bWN-y&_nc_ht=scontent.fcgh5-1.fna&oh=821116c28a7d648b99e82d76ddaa3717&oe=5EB85234"
trich_preto = "https://scontent.fcgh4-1.fna.fbcdn.net/v/t1.15752-9/59305902_430195554472498_1635902160568844288_n.png?_nc_cat=111&_nc_eui2=AeFLlUZ7YEV0Dv2RxNt6OXHPt2Zzp6N-8qvGdwI7R_acSkYTMEQBbnm2r15EyAVEMxU4Q4gZgFeJxjSeBUftUle-r3moQxnQegYn96RIliSTlQ&_nc_ohc=sZwDAcuua9cAX8S8zHf&_nc_ht=scontent.fcgh4-1.fna&oh=8a4436118827ab3cf007bb6877fb1e2c&oe=5EC7E311"
t_preto = "https://scontent.fcgh4-1.fna.fbcdn.net/v/t1.15752-9/59252967_322535588351647_2929346473885696000_n.png?_nc_cat=103&_nc_eui2=AeHcVSuyrCdWbv0iNd0QwrAoGQcWXI9Zg1TUuWQQr5VjBzoishK-pkPhOrBQeyePMd02YbDJbNHD-1CNVEElnGuBTeb96ZfUzGoj_MzjEnSVwA&_nc_ohc=cArGPVLflBcAX9qi8cJ&_nc_ht=scontent.fcgh4-1.fna&oh=08e1fd293f6e15cb12159b65df039a2d&oe=5ED036EE"
t_branco = "https://scontent.fcgh4-1.fna.fbcdn.net/v/t1.15752-9/59475215_300616080837912_840142332341780480_n.png?_nc_cat=101&_nc_eui2=AeGnWAHLRTHPnXKGlnlHp9lKsunUMfYJaTRg3KeF2tvs7Hks0vqETk9uCddOPXIUGyH1woMXWBW6FAgdFDJ15fKv4LipfuKpvr7S8JnFZ1nnng&_nc_ohc=n8ylBMdxCP0AX9DYOIg&_nc_ht=scontent.fcgh4-1.fna&oh=ec9f976b302596adde1cdcc29ef8b7ea&oe=5ECD74CA"


theme = {'font-family': 'Raleway', 'background-color': '#787878'}
colors = {'background': '#111111', 'text': '#7FDBFF'}

def plot_dist_churn(df, col, binary='Churn'):
    tmp_churn = df[df[binary] == 1]
    tmp_no_churn = df[df[binary] == 0]
    tmp_attr = round(tmp_churn[col].value_counts().sort_index() / df[col].value_counts().sort_index(),2)*100
    print(f'Distribution of {col}: ')
    trace1 = go.Bar(
        x=tmp_churn[col].value_counts().sort_index().index,
        y=tmp_churn[col].value_counts().sort_index().values,
        name='Yes_Churn',opacity = 0.8, marker=dict(
            color='seagreen',
            line=dict(color='#000000',width=1)))

    trace2 = go.Bar(
        x=tmp_no_churn[col].value_counts().sort_index().index,
        y=tmp_no_churn[col].value_counts().sort_index().values,
        name='No_Churn', opacity = 0.8, 
        marker=dict(
            color='indianred',
            line=dict(color='#000000',
                      width=1)
        )
    )

    trace3 =  go.Scatter(   
        x=tmp_attr.sort_index().index,
        y=tmp_attr.sort_index().values,
        yaxis = 'y2',
        name='% Churn', opacity = 0.6, 
        marker=dict(
            color='black',
            line=dict(color='#000000',
                      width=2 )
        )
    )
    
    layout = dict(title =  f'Distribution of {str(col)} feature <br>\
                             by Churn Ratio ',
              xaxis=dict(), 
              yaxis=dict(title= 'Count'), 
              yaxis2=dict(range= [0, 100], 
                          overlaying= 'y', 
                          anchor= 'x', 
                          side= 'right',
                          zeroline=False,
                          showgrid= False, 
                          title= 'Percentual Churn Ratio'
                         ))

    fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
    fig.update_layout(title_x=.5, legend_orientation='h', 
                      legend=dict(x=.2, y=-.06))
    return fig

def create_header(some_string):
    header_style = {
        'background-color': theme['background-color'],
        'padding': '1.5rem',
       # 'border-style': 'dotted'
    }
    header = html.Header(html.H1(children=some_string, style=header_style))
    return header

def header_logo():
    h1_title = html.H1(
                    children='Churn Customer Prediction',
                    className="eight columns", 
                    style={#'border-style': 'dotted', 
                           'margin-top':20,
                           'float':'left',
                           'margin-left': 100,
                            #'display':'inline-block'
                            })
    logo_trich = html.Img(
                    src='/assets/fundo_transp.png',
                    className='three columns',
                    style={
                        'height': '14%',
                        'width': '16%',
                        'float': 'right',
                        'padding': 1,
                        'position': 'relative',
                        'margin-top': 26,
                        'margin-bottom':25, 
                        'margin-right': 20,
                        #'border-style': 'dotted', 
                        #'display':'inline-block'

                    })
    return [h1_title, logo_trich]

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

def graph_1():
    graph = html.Div([   
            dcc.Graph(id='Graph1', className="six columns", #style={'border':'dotted'}
                    # figure={'data': [trace0], 
                    #         'layout': layout  
                    #         }
                    ),
            dcc.Graph(id='Graph4', #"Teste only \nbalbalbla\nbalblablbla\nbanbanbanbna\nbmaobjaoboaoj\njaiejaiejaiieja", 
            #style={'border-style': 'dotted', }, 
            className="six columns")
            ])
    return [graph]

def graph2_3():
    graph_2 = html.Div([
                dcc.Graph(id='Graph2',
                        #   figure={'data': [trace0], 
                        #           'layout': layout
                        #          }
                        )], className="four columns")
    graph_3 = html.Div([   
                dcc.Graph(id='Graph3',
                            )], className="eight columns",
                             style={'display':'inline-block'})
    
    return [graph_2, graph_3]

def paragraphs():
    div = html.H1("Ternure")
    paragra = html.P("Blablablabla lbalbalba balbalbalbla balbalbalBlablablabla \
                     lbalbalba balbalbalbla balbalbalBlablablabla lbalbalba\
                     balbalbalbla balbalbalBlablablabla lbalbalba balbalbalbla\
                     balbalbalBlablablabla lbalbalba balbalbalbla balbalbalBlablablabla\
                     lbalbalba balbalbalbla balbalbalBlablablabla lbalbalba balbalbalbla \
                     balbalbalBlablablabla lbalbalba balbalbalbla balbalbal")

    return [div, paragra]

def create_footer():
    p = html.P(
        children=[
            html.Span('Built with '),
            html.A('Plotly Dash',
                   href='https://github.com/plotly/dash', target='_blank'),
            html.Span(' and:'),
        ],
    )

    span_style = {'horizontal-align': 'right', 'padding-left': '1rem'}

    usgs = html.A(
        children=[
            html.I([], className='fa fa-list fa-2x'),
            html.Span('USGS GeoJSON feed', style=span_style)
        ], style={'text-decoration': 'none'},
        href='https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php',
        target='_blank')
    mapbox = html.A(
        children=[
            html.I([], className='fa fa-map-o fa-2x'),
            html.Span('mapbox', style=span_style)
        ], style={'text-decoration': 'none'},
        href='https://www.mapbox.com/', target='_blank')

    font_awesome = html.A(
        children=[
            html.I([], className='fa fa-font-awesome fa-2x'),
            html.Span('Font Awesome', style=span_style)
        ], style={'text-decoration': 'none'},
        href='http://fontawesome.io/', target='_blank')
    datatables = html.A(
        children=[
            html.I([], className='fa fa-table fa-2x'),
            html.Span('jQuery Datatables', style=span_style)
        ], style={'text-decoration': 'none'},
        href='https://datatables.net/', target='_blank')

    ul1 = html.Ul(
        children=[
            html.Li(mapbox),
            html.Li(font_awesome),
            html.Li(datatables),
            html.Li(usgs),
        ],
        style={'list-style-type': 'none'},
    )

    hashtags = 'plotly,dash,usgs'
    tweet = 'Dash Earthquake, a cool dashboard with Plotly Dash!'
    twitter_href = 'https://twitter.com/intent/tweet?hashtags={}&text={}'\
        .format(hashtags, tweet)
    twitter = html.A(
        children=html.I(children=[], className='fa fa-twitter fa-3x'),
        title='Tweet me!', href=twitter_href, target='_blank')

    github = html.A(
        children=html.I(children=[], className='fa fa-github fa-3x'),
        title='Repo on GitHub',
        href='https://github.com/jackdbd/dash-earthquakes', target='_blank')

    li_right_first = {'line-style-type': 'none', 'display': 'inline-block'}
    li_right_others = {k: v for k, v in li_right_first.items()}
    li_right_others.update({'margin-left': '10px'})
    ul2 = html.Ul(
        children=[
            html.Li(twitter, style=li_right_first),
            html.Li(github, style=li_right_others),
        ],
        style={
            'position': 'absolute',
            'right': '1.5rem',
            'bottom': '1.5rem',
        }
    )

    div = html.Div([p, ul1, ul2])
    footer_style = {
        'font-size': '2.2rem',
        'background-color': theme['background-color'],
        'padding': '2.5rem',
        'margin-top': '3rem', 
        'display':'inline-block'
    }
    footer = html.Footer(div, style=footer_style, className='twelve columns')
    return footer

# All functions inside a Div with a specific size
def tab_test1():
    tab1 = html.Div([
        html.Div(header_logo(), className='row', style={ 'display':'inline-block'}), ## Title and logo inline
        html.Div(button_line(), className='row', ), # CheckBoxes e espaço, poderiam estar separados como os gráficos
        html.Div(graph_1(), className='row'), # gráfico principal da tela
        html.Div(paragraphs(), className='row',), # Paragraph of explanation
        html.Div(graph2_3(), className='row', ) # Pie graphs
    ], className="container") # setting the class container to become all in a "box" on the browser. Only header and footer will be out of it
    return tab1

# main APP engine
app.layout = html.Div(children=[
    create_header(app_name), ## Header of the app
    tab_test1(), # Body of the APP
    html.Div(create_footer(), className='twelve columns')]) #create_footer()

@app.callback(
    dash.dependencies.Output('Graph2', 'figure'),
    [dash.dependencies.Input('dropdown2', 'value'),
     dash.dependencies.Input('dropdown', 'value'),])
def plotly_express_test(cat_col, color):
    fig = px.histogram(df_train, x=cat_col, color=color, 
                       #title=f"Distribution of {cat_col} by Churn",
                       
                    # marginal="rug", # can be `box`, `violin`
                    #hover_data=df.columns
                            )
    fig.update_layout(
        title=f"Distribution of {cat_col} by Churn",
        xaxis_title="Value Range Distribution",
        yaxis_title=f"{cat_col} Distribution",
        # font=dict(
        #     #family="Courier New, monospace",
        #     size=15,
        #     #color="#7f7f7f"
        # )
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
    return plot_dist_churn(df_train, cat_col)

def update_graph_src(selector):
    data = go.Bar(
             x=df_train.groupby(selector)['customerID'].count().index,
             y=df_train.groupby(selector)['customerID'].count().values,
             #marker=dict(color=['indianred', 'seagreen'])
             )

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

    figure = go.Figure(data=data, layout=layout)  

    return figure


@app.callback(
    dash.dependencies.Output('Graph3', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('dropdown2', 'value')])
def PieChart(val1, val2, limit=15):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    print(val1, val2)
    # count_trace = df_train[df_cat].value_counts()[:limit].to_frame().reset_index()
    tmp_churn = df_train[df_train['Churn'] == 1].groupby(val1)[val2].sum().nlargest(limit).to_frame().reset_index()
    tmp_no_churn = df_train[df_train['Churn'] == 0].groupby(val1)[val2].sum().nlargest(limit).to_frame().reset_index()
    
    title='tests'

    trace1 = go.Pie(labels=tmp_no_churn[val1], 
                    values=tmp_no_churn[val2], name= "No-Churn", hole= .5, 
                    hoverinfo="label+percent+name+value", showlegend=False,
                    domain= {'x': [0, .48]})

    trace2 = go.Pie(labels=tmp_churn[val1], 
                    values=tmp_churn[val2], name="Churn", hole= .5, 
                    hoverinfo="label+percent+name+value", showlegend=False, 
                    domain= {'x': [.52, 1]})

    layout = dict(title={'text':str(f"Montly Charges representation of {val1}"), 
                         'xanchor':'center', 'yanchor':'top'},
                          height=500, font=dict(size=15), 
                  annotations = [
                      dict(
                          x=.20, y=.5,
                          text='No Churn', 
                          showarrow=False,
                          font=dict(size=20)
                      ),
                      dict(
                          x=.80, y=.5,
                          text='Churn', 
                          showarrow=False,
                          font=dict(size=20)
                      )
        ])

    fig  = go.Figure(data=[trace1, trace2], layout=layout)
    fig.update_layout(title_x=.5)
    return fig


@app.callback(
    dash.dependencies.Output('Graph4', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('dropdown2', 'value')])
def PieChart(val1, val2,limit=15, title='test'):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    df_train['TotalCharges'].fillna(df_train['MonthlyCharges'], inplace=True)
    # count_trace = df_train[df_cat].value_counts()[:limit].to_frame().reset_index()
    tmp_churn = df_train.groupby(val1)[val2].sum().nlargest(limit).to_frame().reset_index()

    trace1 = go.Pie(labels=tmp_churn[val1], 
                    values=tmp_churn[val2], name=str(val1), hole= .5, 
                    hoverinfo="label+percent+name+value", 
                    showlegend=True, 
                    #domain= {'x': [.52, 1]}
                    )

    layout = dict(title={'text':str(f"% of Monhtly Charges \nby {val1}"), 
                         'xanchor':'center', 'yanchor':'top'},
                          height=350, font=dict(size=12), 
                #   annotations = [
                #       dict(
                #           #x=.20, y=.5,
                #           #text='No Churn', 
                #           showarrow=False,
                #           font=dict(size=20)
                #       ),
                    #   dict(
                    #       x=.80, y=.5,
                    #       text='Churn', 
                    #       showarrow=False,
                    #       font=dict(size=20)
                    #   )
        #]
        )
    fig  = go.Figure(data=[trace1], layout=layout)
    fig.update_layout(title_x=.5, #legend_orientation='h', 
                      #legend=dict(x=.3, y=.5))
    )
    fig['layout']['height'] = 530
    fig['layout']['width'] = 520

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)



    