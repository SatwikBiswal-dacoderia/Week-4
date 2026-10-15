d={}
n=int(input("Enter the number of entries : "))
o=0
for i in range(0,n):
    sub=input("Enter the subject : ")
    marks=int(input("Enter the marks : "))
    out=int(input("Enter the out of marks : "))
    o=o+out
    d[sub]=marks
print(d)
c=0
for i in d:
    c=c+d[i]
print("Total marks obtained = ",c)
p=(c/o)*100
print("Total percentage = ",p)
if p>=95:
    print("Grade : A+")
elif p>=90 and p<95:
    print("Grade : A")
elif p>=80 and p<90:
    print("Grade : B+")
elif p>=70 and p<80:
    print("Grade : B")
elif p>=65 and p<=70:
    print("Grade : C")
elif p>=50 and p<65:
    print("Grade : D")
elif p>=34 and p<50:
    print("Grade : E")
else:
    print("Failed!!!")    
