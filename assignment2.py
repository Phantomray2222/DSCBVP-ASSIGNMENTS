#Find the GCD of the given numbers
n=input("enter the first number=")
l=input("enter the second number=")
m=int(n)
o=int(l)
if m>o :
    z=m
else:
    z=o
for i in range(2,z):
     if (z%i) ==0:
        d=i
        print("the factor is ",i)
        
     else :
        continue

print("The GCD is",d)