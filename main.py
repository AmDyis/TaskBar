m = [2,2,1,1,1,2,2, 3, 3, 3, 3, 3, 3, 3, 3 ,3 ,3 ,3, 3]
d = {}
for i in m:
    d[i] = d.get(i, 0) + 1
for i in d:
    if d[i] == max(d.values()):
        print(i)