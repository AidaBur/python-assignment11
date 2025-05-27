from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder()

countries = df['country'].unique()

app = Dash(__name__)
server = app.server 

app.layout = html.Div([
    html.H1("GDP Growth by Country", style={"textAlign": "center"}),
    
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": c, "value": c} for c in countries],
        value="Canada"
    ),
    
    dcc.Graph(id="gdp-growth")
])

@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country):
    filtered_df = df[df["country"] == country]
    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP per Capita Over Time: {country}"
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
