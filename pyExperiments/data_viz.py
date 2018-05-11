import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('gabastil','cswx3939uo')

trace = {'x':[1,2,3,4,5,6], 'y':[1,2,7,3,4,3]}
data = [trace]
layout = {}

fig = go.Figure(data=data, layout=layout)

plot_url = py.plot(fig)
py.plot(fig)