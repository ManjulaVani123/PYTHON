# Online Python compiler (interpreter) to run Python online.
a=int(input("lower range:"))
b=int(input("higher range:"))
for i in range(a,b+1):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count+=1
    if(count==0):
            print(i)