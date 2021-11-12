import pandas as pd
import plotly.express as px

df=pd.read_csv('real_final.csv')

fig1=px.bar(df,x="dwarf name",y='mass',title="StarNames vs Mass")
fig1.show()

fig2=px.bar(df,x="dwarf name",y='radius',title="StarNames vs Radius")
fig2.show()

fig3=px.bar(df,x="dwarf name",y='distance',title="StarNames vs Distance")
fig3.show()

fig4=px.bar(df,x="dwarf name",y='gravity',title="StarNames vs Gravity")
fig4.show()