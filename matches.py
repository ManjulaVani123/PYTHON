import random
no=int(input("enter no.of teams"))
teams=[]
for i in range(no):
    n=input("enter no of teams names")
    teams.append(n)
meet=int(input("enter no of matches"))
matches=[]
for i in range(no-1):
    for j in range(i+1,no):
        for k in range(meet):
            matches.append([teams[i],teams[j]])
random.shuffle(matches)
for i in range(len(matches)):
    print("matches{}:{} vs{}".format(i+1,matches[i][0],matches[i][1]))
