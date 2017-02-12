import pandas as pd
import numpy as np
import os
import csv



#sums up the difference between close and open prices for each day, and tallys the number of each day of the week there was
for filename in os.listdir('data/with_dotw/'):
    count = 0
    tot = [0.0] * 5
    num = [0.0] * 5
    df = pd.read_csv('data/with_dotw/' + filename)
    lst = df["Day of Week"]
    for day in lst:
        tot[day] += (df.get_value(count,"adj_close") - df.get_value(count,"adj_open")) / df.get_value(count, "adj_open")
        num[day] += 1
        count += 1
    with open('data/stats/avg/' + filename, 'w') as outfile: 
        writer = csv.writer(outfile, lineterminator = '\n')
        writer.writerows([num])
        writer.writerows([tot]) 
    outfile.close()



pctdel = [0.0] * 5 #the percent delta average for each day

for filename in os.listdir("data/stats/avg/"):
    with open("data/stats/avg/" + filename) as f:
        days = f.readline().strip().split(',')
        vals = f.readline().strip().split(',')
        for x in range(0,5):
            if float(days[x]) != 0:
                pctdel[x] += float(vals[x])/float(days[x])
    f.close()

print(pctdel)


