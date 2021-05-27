import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random 
import csv

data=pd.read_csv('studentMarks.csv')
data1=data['Math_score'].tolist()

mean=statistics.mean(data1)
std_dev=statistics.stdev(data1)
print("Mean={},Stdev={}".format(mean,std_dev))

# figure=ff.create_distplot([data1],["Math Scores"],show_hist=False)
# figure.show()

def random_set_of_mean():
    dataset=[]
    for i in range(0,100):
        random_index=random.randint(0,len(data1)-1)
        value=data1[random_index]
        dataset.append(value)
    dataset_mean=statistics.mean(dataset)
    return dataset_mean

meanList=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean()
    meanList.append(set_of_means)

meanList_mean=statistics.mean(meanList)
meanList_stdev=statistics.stdev(meanList)
print("Mean List mean={}, Mean List stdev={}".format(meanList_mean,meanList_stdev))


stdev1_start,stdev1_end=meanList_mean-meanList_stdev,meanList_mean+meanList_stdev
stdev2_start,stdev2_end=meanList_mean-2*meanList_stdev,meanList_mean+2*meanList_stdev
stdev3_start,stdev3_end=meanList_mean-3*meanList_stdev,meanList_mean+3*meanList_stdev


#Student using ipad
data_ipad=pd.read_csv('data1.csv')
data1_ipad=data_ipad['Math_score'].tolist()
mean_ipad=statistics.mean(data1_ipad)
std_dev_ipad=statistics.stdev(data1_ipad)
print("Mean={},Std Dev={}",mean_ipad,std_dev_ipad)

#Student doing WS
data_WS=pd.read_csv('data3.csv')
data1_WS=data_WS['Math_score'].tolist()
mean_WS=statistics.mean(data1_WS)
std_dev_WS=statistics.stdev(data1_WS)
print("Mean={},Std Dev={}",mean_WS,std_dev_WS)

#Student taking extra classes
data_class=pd.read_csv('data2.csv')
data1_class=data_class['Math_score'].tolist()
mean_class=statistics.mean(data1_class)
std_dev_class=statistics.stdev(data1_class)
print("Mean={},Std Dev={}",mean_class,std_dev_class)



figure=ff.create_distplot([meanList],["Math Scores"],show_hist=False)
figure.add_trace(go.Scatter(x=[meanList_mean,meanList_mean],y=[0,0.2],name="mean"))
figure.add_trace(go.Scatter(x=[stdev1_start,stdev1_start],y=[0,0.15],mode="lines",name="stdev1_start"))
figure.add_trace(go.Scatter(x=[stdev1_end,stdev1_end],y=[0,0.15],mode="lines",name="stdev1_end"))
figure.add_trace(go.Scatter(x=[stdev2_start,stdev2_start],y=[0,0.15],mode="lines",name="stdev2_start"))
figure.add_trace(go.Scatter(x=[stdev2_end,stdev2_end],y=[0,0.15],mode="lines",name="stdev2_end"))
figure.add_trace(go.Scatter(x=[stdev3_start,stdev3_start],y=[0,0.15],mode="lines",name="stdev3_start"))
figure.add_trace(go.Scatter(x=[stdev3_end,stdev3_end],y=[0,0.15],mode="lines",name="stdev3_end"))
figure.add_trace(go.Scatter(x=[mean_ipad,mean_ipad],y=[0,0.2],name="Mean of Ipad"))
figure.add_trace(go.Scatter(x=[mean_WS,mean_WS],y=[0,0.2],name="Mean of WS"))
figure.add_trace(go.Scatter(x=[mean_class,mean_class],y=[0,0.2],name="Mean of extra class"))
figure.show()










