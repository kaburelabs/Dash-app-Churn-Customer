import dash_bootstrap_components as dbc

# import dash_html_components as html
# import dash_core_components as dcc
from dash import dcc, html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

options_navbar = dbc.Row(
    [
        dbc.Col(
            [
                dcc.Link("Prediction", href="/predictions", className="right8"),
                # dcc.Link("Xplanable AI", href="/explanable")
            ],
            width="auto",
        ),
    ],
    # no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    [
        # Use row and col to control vertical alignment of logo / brand
        dbc.Row(
            [
                dbc.Col(
                    html.A(
                        html.Img(src=PLOTLY_LOGO, height="30px"),
                        href="https://plotly.com",
                        target="blank",
                    )
                ),
                dbc.Col(
                    dbc.NavbarBrand("Churn Analytics & Prediction", className="ml-2")
                ),
            ],
            align="center",
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        dbc.Collapse(options_navbar, id="navbar-collapse", navbar=True, is_open=False),
    ],
    style={"padding":"16px"},
    color="dark",
    dark=True,
)
