
#version 2.0
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

import numpy as np
import pandas as pd
init_notebook_mode(connected=True)
x = np.random.randn(2000)
y = np.random.randn(2000)
fullData=pd.read_csv("C://amit//Learn//Python//GitMcLearningCourseraCode//ipython-notebooks//data//ex1data1.txt", names=['Population','Profit'],header=None)
print(fullData.columns)
print(fullData.head(10))

layout_comp = go.Layout(
    title='Life Expectancy v. Per Capita GDP, 2007',
    hovermode='closest',
    xaxis=dict(
        title='GDP per capita (2000 dollars)',
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Life Expectancy (years)',
        ticklen=5,
        gridwidth=2,
    ),
)

#trsce=go.Figure(data=[go.Scatter(x=fullData['Population'], y=fullData['Profit'])], layout=layout_comp)
#plot(go.Figure(data=[trsce],layout=layout_comp))

plot(fullData['Population'],fullData['Profit'],'go')
#plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])
#plot([go.Scatter(x=fullData['Population'], y=fullData['Profit'])])

#plot([go.Histogram2dContour(x=x, y=y, contours=dict(coloring='heatmap')),
 #      go.Scatter(x=x, y=y, mode='markers', marker=dict(color='white', size=3, opacity=0.3))], show_link=False)