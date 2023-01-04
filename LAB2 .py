

#Task1

num1=int(input('Enter the length of 1st array'))
List1=[]
num2=int(input('Enter the length of 2nd array'))
List2=[]

for i in range(1,num1+1):
    a = int(input('Enter numbers for 1st list'))
    List1.append(a)


for i in range(1,num2+1):
    b=int(input('Enter numbers for 2nd list'))
    List2.append(b)
ListF= List1+List2
ListF.sort()
print("List in sorted order",ListF)



#Task2

num1=int(input('Enter the length of 1st array'))
List1=[]
num2=int(input('Enter the length of 2nd array'))
List2=[]

for i in range(1,num1+1):
    a = int(input('Enter numbers for 1st list'))
    List1.append(a)


for i in range(1,num2+1):
    b=int(input('Enter numbers for 2nd list'))
    List2.append(b)
ListF= List1+List2
ListF.sort()

print('Smallest',min(ListF))
print('Lragest',max(ListF))


#Task3


import math
from math import*
x=float(input("Enter x"))
h=0.001
m=(sin(x+h)-sin(x))/h
n=cos(x)
m=math.ceil(m*100)/100
n=math.ceil(n*100)/100
if(math.isclose(m,n)):
    print("Equal")
else:
    print("Not Equal")
print(m)
print(n)


#Task 4
print('Welcome to the birthday dictionary. We know birthdays of the following people')
Birthdays={'Rabia':'25 Dec','Mishi':'30 Dec', 'Muneeza':'15 Nov'}
for key, value in Birthdays.items():
    print(key)

name=input('Whose birtday do you want to find out')
if name in Birthdays:
    print(Birthdays[name])
else:
    print('No results')


#Task 5
smaple={"name":"kelly","age":"20","Salary":"200000","city":"Lahore"}
keys=["name","age"]
dic2=dict()
for i in keys:
    dic2.update({i:smaple[i]})
print(dic2)
