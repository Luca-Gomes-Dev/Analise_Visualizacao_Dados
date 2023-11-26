from dash import Dash, dcc, html, dash_table, callback, Output, Input
from business.controller import Controller

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?" "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div(
    children=[
        #header
        html.Div(
            children=[
                html.H1(
                    children="Online Shoppers Purchasing Intention",
                    className="header-title",
                ),
                html.P(
                    children=(
                        "Dashboard para analisar os dados das inteções de compras do e-commerce Shoppers"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                #Tabela com os dados
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.P(
                                    "Tabela com os dados",
                                ),
                                html.Hr(),
                            ]
                        ),
                        dash_table.DataTable(
                            id="table-with-some-data",
                            data=Controller.get_grid_data(),
                            page_size=15,
                        ),
                    ],
                    className="table",
                ),
                #Agrupamento de vendas por tipos de usuários.
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.P("Agrupamento dos tipos de usuários e quantidade de vendas"),
                                html.Hr(),
                            ]
                        ),
                        dcc.Graph(
                            id="group-visitors-by-revenue",
                            figure=Controller.get_group_visitors_by_revenue(),
                        ),
                    ],
                    className="card",
                ),
                #Gráfico de barras de Vendas por campo escolhido.
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.P("Quantidade de Vendas por campo escolhido."),
                                html.Hr(),
                                dcc.Dropdown(
                                    options=[
                                        "ExitRates",
                                        "Region",
                                        "BounceRates",
                                        "TrafficType",
                                    ],
                                    value="Region",
                                    id="qtd-revenue-by-field-radio",
                                ),
                            ]
                        ),
                        dcc.Graph(
                            id="qtd-revenue-by-field",
                            figure={},
                        ),
                    ],
                    className="card",
                ),
            
                #Matriz de correlação.
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.P("Matriz de correlação dos dados numéricos"),
                                html.Hr(),
                            ]
                        ),
                        dcc.Graph(
                            id="correlation-matrix",
                            figure=Controller.get_corr_data(),
                        ),
                    ],
                    className="card",
                ),
            
       
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.P("Distribuição por BounceRates"),
                                html.Hr(),
                            ]
                        ),
                        dcc.Graph(
                            id="pie_chart_bounce",
                            figure=Controller.get_pie('BounceRates'),
                        ),
                    ],
                    className="card",
                ),
            
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.P("Distribuição por Exitrates"),
                                html.Hr(),
                            ]
                        ),
                        dcc.Graph(
                            id="pie_chart_exit",
                            figure=Controller.get_pie('ExitRates'),
                        ),
                    ],
                    className="card",
                ),
                 html.Div(
                    [
                        html.Div(
                            children=[
                                html.P("Distribuição por Pagevalues"),
                                html.Hr(),
                            ]
                        ),
                        dcc.Graph(
                            id="pie_page_values",
                            figure=Controller.get_pie("PageValues"),
                        ),
                    ],
                    className="card",
                ),
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.P("Distribuição por Pagevalues"),
                                html.Hr(),
                            ]
                        ),
                        dcc.Graph(
                            id="pie_chart_page",
                            figure=Controller.get_pie('PageValues'),
                        ),
                    ],
                    className="card",
                ),

                 html.Div(
                    [
                        html.Div(
                            children=[
                                html.P("Distribuição por Scattervalues"),
                                html.Hr(),
                            ]
                        ),
                        dcc.Graph(
                            id="scatter_page",
                            figure=Controller.get_scatter('ScatterValues'),
                        ),
                    ],
                    className="card",
                ),
            ],
            className="wrapper",
        ),

        #footer
        html.Div(
            children=[
                html.P(
                    children=(
                        "Copyright © CESAR School 2023 | Todos os direitos reservados."
                    ),
                    className="footer-description",
                ),
            ],
            className="footer",
        ),
    ]
)


@callback(
    Output(component_id="qtd-revenue-by-field", component_property="figure"),
    Input(component_id="qtd-revenue-by-field-radio", component_property="value"),
)
def update_revenue_graph(col_chosen):
    return Controller.get_hist_by_revenue(col_chosen)


if __name__ == "__main__":
    app.run_server(debug=True)
