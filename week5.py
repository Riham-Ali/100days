# Day-27-
x = 30
b = 30
if x > b:
    print("x greater than b")
elif x < b:
    print("b greater than x")

else:
    print("value x=b")

a=90
z=100

print("A=90") if a<z else print("z=100")

if a<z and a<b:
    print("A=90")

if z>a or z>b:
    if z>x:
        print(z)

# Day-28-

i=1
while i<10:
    print("welcome to while Loop")
    if i==5:
        break
    i+=1

j=1
while j<12:
    print(j)
    j += 1
    if i==12:
        continue
else:
    print("last number in the loop")

k=1
while k<5:
    print(k)
    k+=1

# Day-29-

TheList=[6,4,2,0]
for x in TheList:
    print(x)
    if x == 2:
        break


for x in "Riham":
    print(x)


# Day-30-

for x in range(2, 20, 2):
  print(x)
else:
    print("last of loop")

num1="apple","berry"
num2=15,20
for x in num1:
    for y in num2:
        print(x,y)

# Day-31-

def study (names="fahed"):
    print(names+'\t'+"class 1")
study("mohamed")
study("Ahmed")
study("Ali")
study()

# Day-32,33-

for x in range(3,18,1):
    for y in range(2,17,2):
         print(x,y)



