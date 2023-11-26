import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


class Controller:
    """
    Colunas
        Administrative,
        Administrative_Duration,
        Informational,
        Informational_Duration,
        ProductRelated,
        ProductRelated_Duration,
        BounceRates,
        ExitRates,
        PageValues,
        SpecialDay,
        Month,
        OperatingSystems,
        Browser,
        Region,
        TrafficType,
        VisitorType,
        Weekend,
        Revenue
    """

    df = pd.read_csv("data/online_shoppers_intention.csv").sort_values(by="Region")
    df_nums = df.drop(columns=["Month", "VisitorType"])

    @classmethod
    def get_corr_data(cls):
        df_corr = cls.df_nums.corr().round(1)

        fig = go.Figure()
        fig.add_trace(
            go.Heatmap(x=df_corr.columns, y=df_corr.index, z=np.array(df_corr))
        ).update_layout(xaxis_title="Campos", yaxis_title="Valor de correlação")
        return fig

    @classmethod
    def get_grid_data(cls):
        df_fil = cls.df[
            [
                "Administrative_Duration",
                "Informational_Duration",
                "ProductRelated_Duration",
                "BounceRates",
                "ExitRates",
                "PageValues",
                "SpecialDay",
                "Month",
                "Region",
                "VisitorType",
                "Revenue",
            ]
        ]
        df_fil.columns = [
            "Adm Duration",
            "Info Duration",
            "Product Related",
            "Bounce",
            "Exits",
            "Page Values",
            "Special Day",
            "Month",
            "Region",
            "Visitor Type",
            "Revenue",
        ]
        df_res = df_fil.to_dict("records")
        return df_res

    @classmethod
    def get_group_visitors_by_revenue(cls):
        dt_res = px.histogram(
            cls.df, x="VisitorType", color="Revenue", barmode="group"
        ).update_layout(xaxis_title="Tipos de Usuários", yaxis_title="Quantidade")
        return dt_res

    @classmethod
    def get_hist_by_revenue(cls, col_chosen):
        dt_res = px.histogram(
            cls.df_nums, x=col_chosen, color="Revenue", barmode="group"
        ).update_layout(xaxis_title="Campos", yaxis_title="Valor de correlação")
        return dt_res
        
    @classmethod
    def get_pie(cls, col_chosen):
        fig = px.pie(cls.df, values=col_chosen, names="Revenue", hole=.3)
        return fig

    import plotly.express as px


    @classmethod
    def get_scatter(cls, column="Administrative_Duration"):
        fig = px.scatter(cls.df, x="Administrative_Duration", y="Informational_Duration", log_x=True, width=800
        ).update_layout(xaxis_title="Campos", yaxis_title="Valor de correlação")
        return fig

      