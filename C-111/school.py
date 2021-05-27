import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random 
import csv

data=pd.read_csv('School1.csv')
data1=data['Math_score'].tolist()
mean=statistics.mean(data1)
std_dev=statistics.stdev(data1)
print("Mean={},Std Dev={}",mean,std_dev)

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

data_sample1=pd.read_csv('School_1_Sample.csv')
data1_sample1=data_sample1["Math_score"].tolist()
mean_Schoo1_sample1=statistics.mean(data1_sample1)
stdev_Schoo1_sample1=statistics.stdev(data1_sample1)


data_sample2=pd.read_csv('School_2_Sample.csv')
data1_sample2=data_sample1["Math_score"].tolist()
mean_School2_sample2=statistics.mean(data1_sample2)
stdev_School2_sample2=statistics.stdev(data1_sample2)

data_sample3=pd.read_csv('School_3_Sample.csv')
data1_sample3=data_sample3["Math_score"].tolist()
mean_School3_sample3=statistics.mean(data1_sample3)
stdev_School3_sample3=statistics.stdev(data1_sample3)


figure=ff.create_distplot([meanList],["Student Marks"],show_hist=False)
figure.add_trace(go.Scatter(x=[meanList_mean,meanList_mean],y=[0,0.2],name="Mean"))
figure.add_trace(go.Scatter(x=[mean_Schoo1_sample1,mean_Schoo1_sample1],y=[0,0.2],name="School1_Mean"))
figure.add_trace(go.Scatter(x=[mean_School2_sample2,mean_School2_sample2],y=[0,0.2],name="School2_Mean"))
figure.add_trace(go.Scatter(x=[mean_School3_sample3,mean_School3_sample3],y=[0,0.2],name="School3_Mean"))
figure.show()

print("School1+{},School2+{},School3+{}".format(mean_Schoo1_sample1,mean_School2_sample2,mean_School3_sample3))