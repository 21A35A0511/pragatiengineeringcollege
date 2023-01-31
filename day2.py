'''
apple=100
banana=200
pineapple=300
print(apple,end=' ')
print(banana,end=' ')
print(pineapple,end=' ')

print(apple,banana,pineapple)

x, y, z= input("enter the three value:").split('0')
print("total number of students:",x)
print(" number of boys:",y)
print("number of girls:",z)

a=int(input("enter the lemons:"))
b=21
if a<b:
    print()
'''
'''
eml="kumargandhi@gmail.com"
ceml=input("enter the email")
psw=123456
otp=6586
cpsw=int(input("enter the password"))
cotp=int(input("enter the otp:"))
if eml==ceml and psw==cpsw:
    if otp==cotp:
        print("login successful")
    else:
        print("you entered wrong otp")    
else:
    print("login failed")
'''    
 
''' 
a=5
b=True
if 1==b:
    print("yes")
else:
    print("no")
'''    
'''    
a="kumargandhi"
print('s' not in a)
print('s' in a)

for a in range(97,122):
    print(chr(a),end=" ")
'''
'''
for i in range(65,90):
    if i==65 or i==69 or i==73 or i==79 or i==85:
        print(chr(i),end=" ")
 '''       
'''
for i in range(65,90):
    if i!=65 and i!=69 and i!=73 and i!=79 and i!=85:
        print(chr(i),end=" ")
'''

'''
package=84
calls=3000
msgs=100
data=float(2.0)
a=int(input("Enter the day:"))
b=package-a
print("Your plan will expire in",package-a,"days")
tdata=float(input("Enter the data upto used today:"))
print("the",data-tdata,"data left")
ccall=int(input("Enter the calls duration:"))
print("the",calls-ccall,"left")
cmesgs=int(input("Enter the mesgs used upto today:"))
print("the",msgs-cmesgs,"left")
'''
'''
for i in range(1,270):
    if(i%10==0):
        print(i)
'''
'''
for i in range(10,200,20):
    if i%2==0:
        print(i*2)
'''
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")    
'''
'''
for i in range(65,70,2):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print("\n")
'''
'''
for i in range(2,11):
    print(i," * 10" " =",i*10)
'''
i=1
while i<=6:
    j=1
    while j<=i:
        print((i*2-1),end=" ")
        j=j+1
    i=i+1
    print(" ")