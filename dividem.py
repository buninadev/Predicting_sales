
import csv
import os

i = 0
n = 0
once = True
try:
    os.getcwd()
    os.makedirs(os.getcwd()+"/tables")
except Exception:
    pass
file = open('tables/month'+str(i)+'.csv', 'w')
writer = csv.writer(file)

with open('sales_train_v2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if once:
            first = row
            writer.writerow(first)
            once = False
            continue
        n += 1
        if row[1] == str(i):
            print("wait")
            writer.writerow(row)
        else:
            print("ooooooooooooooooooonccccccccccccce")
            i += 1
            file = open('tables/month'+str(i)+'.csv', 'w')
            writer = csv.writer(file)
            writer.writerow(first)
            writer.writerow(row)
