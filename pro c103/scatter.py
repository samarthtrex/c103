import pandas as pd
import plotly.express as px

df=pd.read_csv('scatter_chart.csv')

fig =px.scatter(df,y='cases',x='date',color='country')

fig.show()