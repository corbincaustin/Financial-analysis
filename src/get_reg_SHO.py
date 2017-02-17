import urllib.request
from datetime import date, timedelta as td
import subprocess
import os.path

path = "regsho.finra.org/FNYXshvol"

start_date = date(2016, 3, 1)
end_date = date(2017, 2, 14)
diff = end_date - start_date


for i in range(diff.days + 1):
    curr = start_date + td(days=i)
    yr,mo,day = str(curr).split("-")
    print(yr + mo + day)
    subprocess.Popen(['wget', '-O', os.path.join("../data/regsho", yr + "_" + mo + "_" +  day), path + yr + mo + day + ".txt"])
    

    
    
    #urllib.request.urlretrieve(path + yr + mo + day + ".txt")
    #with open("../data/regsho/" + yr + mo + day, 'w') as outfile:
    #    for line in urllib.request.urlopen(path + yr + mo + day + ".txt"):
    #        outfile.write(line)
    
    #outfile.close()
    





