import random
sample = []
n = int(input())
for x in range(n):
    sample.append(random.randrange(0,10))

with open('Lists', 'w') as f:
    for item in sample:
        f.write("%d " % item)
f.close()