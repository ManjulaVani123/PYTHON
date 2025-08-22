a=["ram","sahithi","maneesha","chinni"]
marks=[[45,67,98,48],[20,98,76,32],[60,18,87,68],[30,45,89,96]]
total=4
for i in range(4):
    s=sum(marks[i])
    percentage=(s//total)
    print("{}.{}:{} %".format(i+1,a[i],percentage))