import pandas as pd 
import csv
import plotly.graph_objects as go

file = pd.read_csv("./data.csv")
#print(file)

fs= file.loc[file['student_id'] == 'TRL_987']
print(fs)

group = fs.groupby("level")["attempt"].mean()
print(group) 

graph = go.Figure(go.Bar(x = group, y = ["Level1", "Level2","Level3","Level4"], orientation = "h"))
graph.update_layout(title = "Student: TRL_987")
graph.update_xaxes(title = "Average")
graph.update_yaxes(title = "Levels")
graph.show()
