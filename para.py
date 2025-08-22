import random
d=[22,33,45,67,22,33]
l=[]
for i in range(len(d)):
    if(d[i] not in l):
        l.append(d[i])
print(l)
        
