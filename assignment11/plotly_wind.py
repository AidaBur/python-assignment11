import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type='pandas')

print("FIRST 10 ROWS:")
print(df.head(10))
print("\nLAST 10 ROWS:")
print(df.tail(10))

strength_map = {
    "0-1": 0.5,
    "2-3": 2.5,
    "4-5": 4.5,
    "6+": 6.0
}

df["strength"] = df["strength"].map(strength_map)

fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs Frequency by Direction",
    hover_data=["direction"]
)

fig.write_html("wind.html", auto_open=True)
