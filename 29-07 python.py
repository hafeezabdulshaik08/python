# 1 (1) program to find sum of a natural numbers using while loop
n=int(input("enter the value:"))
sum=0
i=1
while i<=n:
	sum+=i
	i+=1
print("the sum =",sum)	




#1 (2) PROGRAM TO FIND N NATURARAL NUMERS USING FOR LOOP
n=int(input("ENTER THE N VALUE:"))
sum=0
for i in range(1,n+1):
	sum+=i
	i+=1
print("sum=",sum)	



#2 (1) program using for loop
n=int(input("ENTER THE N VALUE:"))

for i in range(1,11):
	mul=n*i
print(mul)	

#2 (2) program using for loop
n=int(input("ENTER THE N VALUE:"))
i=1
while i<=10:
	mul=n*i
	print(mul)
	i+=i

#3 write aprogram to find string lenth
n=str(input("enter the string:"))
for i in n:
	print(i)
print("string length:",len(n))	



#programn to print the multiplication table
n=int(input("enter the value:"))
i=1
while i<=10:
	mul=n*i
	print(mul)
	i+=1	

#4 programn to find factorial of a given number
n=int(input("enter the value:"))
fac=1
for i in range(1,n+1):
	fac*+i
print("the factorial=",fac)	

# 5 programn to find  given  number is prime or not
n=int(input("enter the value:"))
j=0
for i in range(1,n+1):
	if n%1==0:
		j+=1
if j==2:	
	print("prime number")
else:
	print(" not a prime number")	
				

