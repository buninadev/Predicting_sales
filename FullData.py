import csv
import os

"""
file = open("FullData.csv",'w')
writer= csv.writer(file)

os.chdir("month_sales")
for file in os.listdir(os.getcwd()):
    month=open(file,'r')
    Read=csv.reader(month)
    i=0
    for row in Read:
        if i==0:
            i=1
            continue
        if row != "":
            writer.writerow(row)

"""
import pandas as pd
df = pd.read_csv('FullData.csv')
df.to_csv('output.csv', index=False)
    


