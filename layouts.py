

import dash_core_components as dcc
import dash_html_components as html

theme = {'font-family': 'Raleway', 'background-color': '#787878'}


def graph_1():
    graph = html.Div([   
            dcc.Graph(id='Graph1', 
                      className="six columns", 
                      #style={'border':'dotted'}
                    ),
            dcc.Graph(id='Graph4', 
            #style={'border-style': 'dotted', }, 
            className="six columns", )
            ])
    return [graph]


def graph2_3():
    graph_2 = html.Div([
                dcc.Graph(id='Graph2',
                        )], className="four columns")
    graph_5 = html.Div([
                dcc.Graph(id='Graph5',
                        )], className="four columns")
    graph_3 = html.Div([   
                dcc.Graph(id='Graph3',
                        )], className="four columns")

    # Return of the graphs in all the row
    return [graph_2, graph_3, graph_5]


def create_footer():
    p = html.P(
        children=[
            html.Span('Developed By: '),
            html.A('trich.ai | Data Intelligence Solutions',
                   href='https://trich.ai', target='_blank'),
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
            html.Li(mapbox, style={'display':'inline-block'}),
            html.Li(font_awesome, style={'display':'inline-block'}),
            html.Li(datatables, style={'display':'inline-block'}),
            html.Li(usgs, style={'display':'inline-block'}),
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

    div = html.Div([p, ul1, ul2],)
    footer_style = {
        'font-size': '2.2rem',
        'background-color': 'rgb(191, 208, 247)',
        #'padding': '2.5rem',
        'margin-top': '3rem', 
        'display':'inline-block'
        
    }
    footer = html.Footer(div, style=footer_style, className='twelve columns')
    return footer


def create_header(some_string):
    header_style = {
        'background-color':'rgb(191, 208, 247)',
        'padding': '1.5rem',
        'display':'inline-block',
        'width':'100%'
        
       # 'border-style': 'dotted'
    }
    logo_trich = html.Img(
                    src='/assets/fundo_transp.png',
                    className='three columns',
                    style={
                        'height': 'auto',
                        'width': '180px',
                        'float': 'right',
                        # 'padding': 1,
                        #'position': 'relative',
                        'margin-right': '54px' ,
                        #'border-style': 'dotted', 
                        'display':'inline-block'})

    title = html.H1(children=some_string, className='eight columns', style={'margin':'0 0 0 24px', 'font-size':'43px'})

    header = html.Header(html.Div([title, logo_trich]), style=header_style)

    return header

def header_logo():
    h1_title = html.H1(
                    children='Churn Customer Prediction',
                    #className="eight columns", 
                    style={#'border-style': 'dotted', 
                           'margin-top':20,
                           #'float':'left',
                           #'margin-left': 100,
                           'font-size':'50px'
                            #'display':'inline-block'
                            })

    subtitle = html.Div(dcc.Markdown('''
    **Churn rate**, when applied to a customer base, refers to the proportion of contractual customers or subscribers who leave a supplier during a given time period. It is a possible indicator of customer dissatisfaction, cheaper and/or better offers from the competition, more successful sales and/or marketing by the competition, or reasons having to do with the customer life cycle.
            
    When talking about subscribers or customers, sometimes the expression **"survival rate"** is used to mean 1 minus the churn rate. For example, for a group of subscribers, an annual churn rate of 25 percent is the same as an annual survival rate of 75 percent. Both imply a customer lifetime of four years. I.e., a customer lifetime can be calculated as the inverse of that customer's predicted churn rate. For a group or segment of customers, their customer life (or tenure) is the inverse of their aggregate churn rate. Gompertz distribution models of distribution of customer life times can therefore also predict a distribution of churn rates.

'''),  style={'margin':'0 auto',# 'padding-left':'35px'
})

    return [h1_title, subtitle]

def paragraphs():
    div = html.H1("Revenue Churn", style={'width':'85%', 'margin':'0 auto'})
    
    paragra = html.P(dcc.Markdown("**Revenue churn** is the monetary amount of recurring revenue lost in a period divided by the total revenue at the beginning of the period. Revenue churn is commonly used in Software as a Service (SaaS) and other business models that rely on recurring revenue models."), 
    style={'width':'85%', 'margin':'0 auto'})

    return [div, paragra]

