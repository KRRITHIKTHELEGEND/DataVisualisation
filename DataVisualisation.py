import pandas as pd
import plotly.express as px

something = pd.read_csv('C:\Users\prash\AppData\Local\Programs\Python\Python39\line_chart.csv')

fig = px.scatter(something, x='date', y='cases', color='country')
fig.show()