import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

df = pd.read_csv('/content/metadata.csv')

df.columns = df.columns.str.strip()

print("Available columns in dataset:", df.columns)

correct_x_column = 'Capacity'
correct_re_column = 'Re'
correct_rct_column = 'Rct'

fig = make_subplots(rows=3, cols=2, subplot_titles=(
    "Line Chart: Re vs Capacity", 
    "Scatter Plot: Rct vs Capacity", 
    "Histogram: Capacity Distribution", 
    "Box Plot: Re", 
    "Pie Chart: Distribution of Battery IDs", 
    "Scatter Plot: Re vs Rct"))

fig.add_trace(go.Scatter(
    x=df[correct_x_column],
    y=df[correct_re_column],
    mode='lines',
    name='Line Chart: Re',
    line=dict(color='royalblue')
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=df[correct_x_column],
    y=df[correct_rct_column],
    mode='markers',
    name='Scatter Plot: Rct',
    marker=dict(color='seagreen', size=8)
), row=1, col=2)

fig.add_trace(go.Histogram(
    x=df[correct_x_column],
    name='Histogram: Capacity',
    marker=dict(color='darkorange')
), row=2, col=1)

fig.add_trace(go.Box(
    y=df[correct_re_column],
    name='Box Plot: Re',
    marker=dict(color='mediumpurple')
), row=2, col=2)

fig.add_trace(go.Scatter(
    x=df[correct_re_column],
    y=df[correct_rct_column],
    mode='markers',
    name='Scatter Plot: Re vs Rct',
    marker=dict(color='firebrick', size=8)
), row=3, col=2)

fig.update_xaxes(title_text='Capacity', row=2, col=1)
fig.update_xaxes(title_text='Re (Ohms)', row=1, col=1)
fig.update_xaxes(title_text='Re (Ohms)', row=3, col=2)

fig.update_yaxes(title_text='Re (Ohms)', row=1, col=1)
fig.update_yaxes(title_text='Rct (Ohms)', row=1, col=2)
fig.update_yaxes(title_text='Capacity', row=2, col=1)
fig.update_yaxes(title_text='Re (Ohms)', row=2, col=2)
fig.update_yaxes(title_text='Rct (Ohms)', row=3, col=2)

fig.update_layout(
    height=1000, 
    width=1200, 
    title_text="Battery Parameter Plots with Colors",
    showlegend=False,
    plot_bgcolor='rgba(240,240,240,0.95)'
)

fig.show()
