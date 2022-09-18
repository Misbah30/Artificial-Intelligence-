#Tasl 1
n=int(input('Enter an integer'))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)

#Tasl 2
list=[1,2,3,4,5]
even_list=[]
odd_list=[]
sum_even=0
sum_odd=0
odd=0
even=0
sum_odd=0
for even in list:
    if(even%2==0):
        even_list.append(even)
print("Even num",even_list)
for i in range (0,len(even_list)):
    sum_even= sum_even +even_list[i]
print("Sum of even num",sum_even)
for odd in list:
    if(odd%2==1):
        odd_list.append(odd)
print("Odd num",odd_list)
    
for j in range (0,len(odd_list)):
    sum_odd= sum_odd +odd_list[i]
print("Sum of odd num",sum_odd)

#Tasl 3
n=int(input("Enter the range"))
i=0
f=0
s=1
while(i< n):
    if(i<=1):
        Next=i
    else:
        Next=f+s
        f=s
        s= Next
    print(Next)
    i=i+1

#Tasl 4
print("Enter your marks in following subjects")
a=int(input("Maths"))
b=int(input("English"))
c=int(input("Science"))
d=int(input("Pakstd"))
e=int(input("Urdu"))
Sum= a+b+c+d+e
avg= Sum/5
print("Average",avg)
if avg>=91 and avg<=100:
    print("Your Grade is A")
elif avg>=81 and avg<=90:
    print("Your Grade is B")
elif avg>=71 and avg<=80:
    print("Your Grade is C")
elif avg>=61 and avg<=70:
    print("Your Grade is D")
elif avg>=50 and avg<=60:
    print("Your Grade is E")
elif  avg<50:
    print("Your Grade is F")
else:
    print("Error")

#Tasl 5
n=int(input("Enter a number"))
f=1
if n<0:
    print("error")
elif n==0:
    print("factorial is 1")
else:
    for i in range(1,n+1):
        f=f*i
    print("factorial of",n,"is",f)


