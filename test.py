import pandas as pd
import numpy as bp
from datetime import date


csv = pd.read_csv("data/csvs/AAPL")

dates = csv.ix[:,0]

dayvals = [] * len(csv.index)
for d in dates:
    year,month,day = d.split("-")

    daynum = date(int(year), int(month), int(day)).weekday()
    #print("date is assigned " + str(daynum))
    dayvals.append(daynum)

print(dayvals)


