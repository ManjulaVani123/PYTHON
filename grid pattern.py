n=int(input())
a=[["A" for i in range(n+2)]for i in range(n+2)]
for i in range(n+2):
    for j in range(n+2):
        if(i==0 or i==n+1 or j==0 or j==n+1):
            a[i][j]="A"
        elif(i%2!=0):
            a[i][j]="*"
        elif(i%2==0):
            a[i][j]="$"
for i in range(n+2):
    for j in range(n+2):
        print(a[i][j],end="")
    print()
   