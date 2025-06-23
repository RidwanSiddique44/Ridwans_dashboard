import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Sample data
data = {
    "Product Name": ["Bluetooth Speaker", "Wireless Mouse", "LED Monitor", "Laptop Stand",
                     "Gaming Keyboard", "USB-C Cable", "Web Camera", "External SSD",
                     "Office Chair", "Smartphone Case"],
    "Unit Price": [45, 25, 150, 30, 70, 12, 60, 100, 180, 15],
    "Discount (%)": [10, 5, 15, 20, 10, 0, 12, 18, 25, 5],
    "Units Sold": [120, 200, 40, 75, 90, 300, 65, 50, 35, 150],
    "Total Sale": [4860, 4750, 5100, 1800, 5670, 3600, 3432, 4100, 4725, 2137.5],
    "Profit": [1440, 1300, 900, 600, 1980, 1200, 1105, 1300, 1575, 500],
    "Stock Left": [30, 50, 10, 25, 15, 200, 8, 12, 5, 60]
}
df = pd.DataFrame(data)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Sales Dashboard"

# Define layout
app.layout = html.Div(style={
    'fontFamily': 'Arial',
    'backgroundColor': '#000000',
    'padding': '20px',
    'color': '#ffffff'
}, children=[
    html.H1("📊 Product Sales Dashboard", style={'textAlign': 'center', 'color': '#ffffff'}),

    html.Div(style={
        'display': 'flex',
        'flexWrap': 'wrap',
        'justifyContent': 'space-around',
        'gap': '20px'
    }, children=[

        html.Div(style={'flex': '1 1 45%', 'backgroundColor': '#000000', 'padding': '10px'}, children=[
            dcc.Graph(
                figure=px.bar(df, x="Product Name", y="Total Sale", color="Product Name",
                              title="Total Sales by Product", template='plotly_dark')
            )
        ]),

        html.Div(style={'flex': '1 1 45%', 'backgroundColor': '#000000', 'padding': '10px'}, children=[
            dcc.Graph(
                figure=px.pie(df, names="Product Name", values="Profit", title="Profit Distribution",
                              template='plotly_dark')
            )
        ]),

        html.Div(style={'flex': '1 1 45%', 'backgroundColor': '#000000', 'padding': '10px'}, children=[
            dcc.Graph(
                figure=px.scatter(df, x="Units Sold", y="Profit", size="Unit Price",
                                  color="Product Name", hover_name="Product Name",
                                  title="Profit vs Units Sold", template='plotly_dark')
            )
        ]),

        html.Div(style={'flex': '1 1 45%', 'backgroundColor': '#000000', 'padding': '10px'}, children=[
            dcc.Graph(
                figure=px.line(df, x="Product Name", y="Stock Left", title="Remaining Stock",
                               markers=True, line_shape="spline", template='plotly_dark')
            )
        ])
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
