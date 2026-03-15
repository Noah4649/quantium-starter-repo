import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"])
daily_sales = df.groupby("date", as_index=False)["sales"].sum()
daily_sales = daily_sales.sort_values("date")

fig = px.line(daily_sales, x="date", y="sales", title="Daily Sales of Pink Morsel", labels={"date": "Date", "sales": "Sales"})
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"), 
    dcc.Graph(figure=fig)
    ])
if __name__ == "__main__":
    app.run(debug=True)