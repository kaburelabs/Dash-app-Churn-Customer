
import plotly.graph_objs as go
from dash import dcc, html


def plot_dist_churn2(df, col):

    tmp_attr = df[col].value_counts()

    trace1 = go.Bar(
        x=tmp_attr.sort_index().index,
        y=tmp_attr.sort_index().values,
        # name='Yes_Churn',
        opacity=0.8, marker=dict(
            color='seagreen',
            line=dict(color='#000000', width=1)))

    layout = dict(title=f'Distribution of {str(col)}',
                  xaxis={'type': 'category'},
                  yaxis=dict(title='Count'))

    fig = go.Figure(data=[trace1], layout=layout)
    fig.update_layout(title_x=.5,
                      legend_orientation='h',
                      # height=450,
                      autosize=True,
                      legend=dict(x=.8, y=-.06))

    return fig


def plot_dist_churn(df, col, binary='Churn'):
    tmp_churn = df[df[binary] == 1]
    tmp_no_churn = df[df[binary] == 0]
    tmp_attr = round(tmp_churn[col].value_counts().sort_index(
    ) / df[col].value_counts().sort_index(), 2)*100
    # print(f'Distribution of {col}: ')
    trace1 = go.Bar(
        x=tmp_churn[col].value_counts().sort_index().index,
        y=tmp_churn[col].value_counts().sort_index().values,
        name='Churn', opacity=0.8, marker=dict(
            color='seagreen',
            line=dict(color='#000000', width=1)))

    trace2 = go.Bar(
        x=tmp_no_churn[col].value_counts().sort_index().index,
        y=tmp_no_churn[col].value_counts().sort_index().values,
        name='No Churn', opacity=0.8,
        marker=dict(
            color='indianred',
            line=dict(color='#000000',
                      width=1)
        )
    )

    trace3 = go.Scatter(
        x=tmp_attr.sort_index().index,
        y=tmp_attr.sort_index().values,
        yaxis='y2',
        name='%Churn', opacity=0.6,
        marker=dict(
            color='black',
            line=dict(color='#000000',
                      width=2)
        )
    )

    layout = dict(title=f'Distribution of {str(col)} feature <br>by Churn Ratio ',
                  xaxis=dict(),
                  yaxis=dict(title='Count'),
                  yaxis2=dict(range=[0, 100],
                              overlaying='y',
                              anchor='x',
                              side='right',
                              zeroline=False,
                              showgrid=False,
                              title='Percentual Churn Ratio'
                              ))

    fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

    fig.update_layout(title_x=.5,
                      legend_orientation='h',
                      # height=450,
                      autosize=True,
                      legend=dict(x=.002, y=-.06))
    return fig


def pie_norm(df, val1, val2, limit=15):
    tmp = df.groupby(val1)[val2].sum().nlargest(limit).to_frame().reset_index()
    tmp = tmp.sort_values(val1)

    trace1 = go.Pie(labels=tmp[val1], sort=False,
                    # textposition='outside',
                    # legendgroup='True',
                    # textpositionsrc='outside',
                    values=tmp[val2], name=str(val1), hole=.5,
                    hoverinfo="label+percent+name+value",
                    # showlegend=True,
                    #domain= {'x': [.52, 1]}
                    )

    layout = dict(title={'text': str(f"{val2} Ratio of <br>{val1} by General")},
                  #         'xanchor':'center', 'yanchor':'top'},
                  #          height=350, font=dict(size=12),
                  annotations=[
                      dict(
                          text='%General',
                          showarrow=False,
                          font=dict(size=15)
                      )
    ], titlefont={'size': 15}  # sort=False
    )
    fig = go.Figure(data=[trace1], layout=layout)

    fig.update_layout(title_x=.5, height=320,
                      legend_orientation='h',
                      autosize=True,
                      margin=dict(t=65, b=35, r=35, l=35))

    #fig['layout']['height'] = 380
    # fig['layout']['width'] = 350

    return fig


def pie_churn(df, val1, val2, binary, limit=15):

    if binary == 'Churn':
        bina = 1
    else:
        bina = 0

    tmp = df[df['Churn'] == bina].groupby(
        val1)[val2].sum().nlargest(limit).to_frame().reset_index()

    tmp = tmp.sort_values(val1)

    trace1 = go.Pie(labels=tmp[val1], sort=False,
                    values=tmp[val2], name=f'{binary}', hole=.5,
                    hoverinfo="label+percent+name+value", showlegend=True,
                    #domain= {'x': [0, .48]}
                    )

    layout = dict(title={'text': str(f"{val2} Ratio of <br>{val1} by {binary}")},
                  # 'xanchor':'center', 'yanchor':'top'},
                  #  height=500, font=dict(size=15),
                  annotations=[
                      dict(
                          #      x=.20, y=.5,
                          text=f'%{binary}',
                          showarrow=False,
                          font=dict(size=15)
                      )
    ], titlefont={'size': 15})

    fig = go.Figure(data=[trace1], layout=layout)

    fig.update_layout(title_x=.5, height=320,
                      legend_orientation='h',
                      autosize=True,
                      margin=dict(t=65, b=35, r=35, l=35),)
    # fig['layout']['height'] = 380
    #fig['layout']['width'] = 350

    return fig
