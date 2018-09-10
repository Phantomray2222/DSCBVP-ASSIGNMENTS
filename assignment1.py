#Print numbers till n
print("enter the postitive integer you want upto which you want to find out prime numbers ")
n=input('Enter your input:') 
print("you have chosen till " + n)
z=int(n)
for i in range(2,z):
      if (z % i ) ==0:
        print("it is not a prime number")
        break
      else :
        print("it is  a prime number")
        break