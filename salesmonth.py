import os
import csv


for i in range(0, 34):
    items = {}

    once = True
    try:
        os.getcwd()
        os.makedirs(os.getcwd()+"/month_sales")
    except Exception:
        pass
    file = open("month_sales/month_sales"+str(i)+".csv", 'w')
    writer = csv.writer(file)

    with open("tables/month"+str(i)+".csv", newline='') as msales:
        reader = csv.reader(msales)
        for row in reader:
            if row != []:
                if once:
                    writer.writerow(["Item_id", "Month_sales", "month"])
                    once = False
                    continue
                if str(row[3]) in items:
                    items[str(row[3])] += float(row[5])
                else:
                    items[str(row[3])] = float(row[5])
    print(items)

    for x, y in items.items():
        writer.writerow([x, y, i])

    file.close()
