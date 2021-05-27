import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random 
import csv

data=pd.read_csv('data1.csv')
data1=data['Math_score'].tolist()
mean=statistics.mean(data1)
std_dev=statistics.stdev(data1)
print("Mean={},Std Dev={}",mean,std_dev)