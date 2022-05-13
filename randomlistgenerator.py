import random
sample = []
n = int(input())
for x in range(n):
    sample.append(random.uniform(0.0,1.0))

with open('List0-1x1.0003', 'w') as f:
    for item in sample:
        f.write("%f " % item)
f.close()
