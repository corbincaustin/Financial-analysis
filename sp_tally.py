import pandas as pd
import numpy as np
import os
import csv





pctdel = [0.0] * 5 #the percent delta average for each day

for filename in os.listdir("data/stats/avg/"):
    with open('data/sp500') as f1:
        for line in f1:
            if filename in line:
                with open("data/stats/avg/" + filename) as f:
                    days = f.readline().strip().split(',')
                    vals = f.readline().strip().split(',')
                    for x in range(0,5):
                        if float(days[x]) != 0:
                            pctdel[x] += float(vals[x])/float(days[x])
                f.close()
        f1.close()

print(pctdel)


