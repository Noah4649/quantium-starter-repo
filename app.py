import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"), 
    dcc.RadioItems(id="region-filter", 
                   options=[{"label": "All", "value": "All"}, 
                            {"label": "North", "value": "north"}, 
                            {"label": "South", "value": "south"}, 
                            {"label": "East", "value": "east"}, 
                            {"label": "West", "value": "west"}],
                            value="All",
                            inline=True
                    ),
    dcc.Graph(id="sales-graph")
])

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    if selected_region == "All":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]
    
    daily_sales = filtered_df.groupby("date", as_index=False)["sales"].sum().sort_values("date")
    fig = px.line(daily_sales, x="date", y="sales", title="Daily Sales of Pink Morsel over Time", labels={"date": "Date", "sales": "Sales ($)"})
    return fig

if __name__ == "__main__":
    app.run(debug=True)