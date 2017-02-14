import pandas as pd
import numpy as bp
from datetime import date
import os

for filename in os.listdir('../data/raw/'):
    print(filename)
    csv = pd.read_csv('../data/raw/' + filename)

    dates = csv.ix[:,0]

    dayvals = [] * len(csv.index)
    days = [] * len(csv.index)
    for d in dates:
        year,month,day = d.split("-")

        daynum = date(int(year), int(month), int(day)).weekday()
        #print("date is assigned " + str(daynum))
        dayvals.append(daynum)
        days.append(day)


    csv["Day of Week"] = dayvals
    csv["Day"] = days
    csv.to_csv('../data/with_dotw/' + filename)
