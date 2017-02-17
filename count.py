import os
count = 0
for filename in os.listdir("data/raw/"):
    with open("data/raw/" + filename, 'r') as f:
        for line in f:
            count+=1


print(count)
