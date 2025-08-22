students=["anu","manju","swetha","vikas","sameera"]
cgpa=[59,67,89,97,52]
arrear=[0,1,2,0,0]
for i in range(4):
    if( (arrear[i]==0) and (cgpa[i]>60)):
        print(students[i])