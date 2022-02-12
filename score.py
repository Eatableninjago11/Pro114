import plotly.express as px
import pandas as pd
import csv
import numpy as np

df = pd.read_csv("main.csv")
TOEFL_Score = df["TOEFL Score"].tolist()
chance_of_admit = df["Chance of Admit "].tolist()

fig = px.scatter(x=TOEFL_Score, y=chance_of_admit)
fig.show()

m = 0.01
c = -2.5
y = []

for x in TOEFL_Score:
    y_value = m*x+c
    y.append(y_value)
    
fig = px.scatter(x=TOEFL_Score, y=chance_of_admit)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_Score), x1= max(TOEFL_Score)
    )
])
fig.show()

TOEFL_Score_array = np.array(TOEFL_Score)
chance_of_admit_array = np.array(chance_of_admit)

m, c = np.polyfit(TOEFL_Score_array,chance_of_admit_array,1)

y=[]

for x in TOEFL_Score_array:
  y_value = m*x+c
  y.append(y_value)

fig = px.scatter(x=TOEFL_Score_array, y=chance_of_admit_array)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_Score_array), x1= max(TOEFL_Score_array)
    )
])
fig.show()