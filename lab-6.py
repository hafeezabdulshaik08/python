def arth(m,n):
	op=int(input("enter 1-add,2-mul,3-div,4-sub"))
	match op:
		case 1: return(m+n)
		case 2: return(m*n)
		case 3: return(m/n)
		case 4: return(m-n)
a=int(input("enter a:"))
b=int(input("enter b:"))
print(arth(a,b))		






'''#def gcd(a,b):
	if a==b:
		return a
	elif a<b:
		return gcd(b,a)
	else:
		return gcd(b,a-b)
a=int(input())
b=int(input())
print(gcd(a,b))'''
import math
n=int(input("enter the value of n:"))
m=int(input("enter the value of m:"))
print("GCD of {n} and {m} is:",math.gcd(m,n))
	
