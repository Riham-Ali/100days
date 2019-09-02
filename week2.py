# day-6-
A = int('4')
B = float(5)
C = str(19.5)
print(A)
print(B)
print(C)

# day-7-
print('this with a single quotation')
print("this with a double quotation")
D = "Hi"
print(D)
E = """ this example
for multiline """
print(E)
C = "hello"
print(C[3])
print(C[1:4])

# day-8-
F = "  Hello , World  "
print(F.strip())
print(len(F))
print(F.lower())
print(F.upper())
print(F.replace("o","w"))
print(F.split(","))

# day-9-
name = "my name is riham and my BD  {2} {1} {0}"
day = 17
month = 12
year = 1998
print(name.format(day , month , year))


# day-10-
G = 10
H = 4
# لضرب عددين
print(G*H)
# طرح عددين
print(G-H)
# جمع
print(G+H)
# قسمه
print(G/H)
#
print(G%H)
# عملية أُسية
print(G**H)
#
print(G//H)
G+=4
print(G)
print(G>=H)


# day-11-
I = "hello"
print(G<H and G!=H)
print("hello" in I)

#day -12-
J = " Please, I want {} sandwishes and {} donutes"
J = J.replace("I","we")
J = J.replace("a","A")
J= J.format(5,7)
print(J)
