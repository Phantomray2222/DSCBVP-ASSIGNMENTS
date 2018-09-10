#Palindrome
a=input("Enter the string name here ")
length=len(a)-1
loopcount=0
while(loopcount<=length):
    if(a[loopcount]==a[length-loopcount]):
        
            print("The string is a palindrome")
            break
    else:
        print ("The string is not a palindrome")
        break
    loopcount+=1