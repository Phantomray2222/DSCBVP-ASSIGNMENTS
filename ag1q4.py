#question4
#part1
a=[5,7,9,3,2,1,4,2,6,3,0,9,8]
for i in a:
    if i<5:
        print(i)

#part2
y=[]
y=[i for i in a if i<5]
print(y)

#part3
#used above 

#part4
z=input("enter a number here")
n=int(z)
a=[5,7,9,3,2,1,4,2,6,3,0,9,8]
for i in a:
    if i==n:
        print("number present")
        break
else:
    print("number cannot be found")   
        