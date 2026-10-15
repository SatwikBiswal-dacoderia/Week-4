d={}
n=int(input("Enter the number of entries : "))
for i in range(0,n):
    name=input("Enter the name : ")
    marks=int(input("Enter the marks obtained : "))
    d[name]=marks
print(d)
for i in d:
    if d[i]>60:
        print(i)
