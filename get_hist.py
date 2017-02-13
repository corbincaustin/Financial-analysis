import intrinio
import pandas as pd
import numpy as np
import requests.exceptions
import sys


# prints a dataframe
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')



start_line = 0


#gets the last line where the script stopped
try:
    with open('./data/start_line.txt', 'r') as sl: start_line = int(sl.read())
except:
    pass

print(start_line)


# reads the file of all stocks, retrieves symbol, uses intrinio api to retrieve historical data from january 1, 2016 to present, and writes to csv

with open("./data/all_stocks.txt", "r") as f:
    for i, line in enumerate(f):
        if i < start_line: continue # passes through until last line parsed is reached
        print(line)
        sym,rest = line.split("|",1) # retrieves symbol
        print(sym)


        try:
            x = intrinio.prices(sym)
            x.to_csv('data/raw/' + sym)

        except requests.exceptions.HTTPError as err:

            # if the api limit is reached, write ending line and exit
            if err.response.status_code == 429:
                print("limit reached at line " + str(i) + "...exiting")
                with open('./data/start_line.txt', 'w') as outfile: outfile.write(str(i))
                sys.exit()
            else:
                print("error with " + sym + ", code: " + err.code)

        except AttributeError:
            print("error with " + sym)

    



f.close()






#x = intrinio.get('companies', identifier='GOOG')
#temp = 'AAPL'
#temp = 'data/' + temp



#print_full(x)




