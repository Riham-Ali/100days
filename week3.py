# day-13-
TheList = [1.5,2.5,3.5,4.5,5.5]
print(TheList)
print(TheList[3])
for x in TheList:
    print(x)
TheList[0]=2
print(TheList[0])
del TheList[0]
print(TheList)
del TheList

# day-14-
color = ["black"]*9
print(color[0:5])
if "black" in color:
    print("black in the list of color")


# day-15-
print(len(color))
color.append("pink")
color.insert(5,"orange")
print(color)
color.remove("black")
print(color)
color.pop()
color.pop(4)
print(color)
newColor=color.copy()
color.clear()
print(color+newColor)
num=list((1,2,3,4,5))
print(num)


# day-16-
TheTuble=(2.5,3.5,4,6,"riham")
print(TheTuble[1:4])
for x in TheTuble:
    print(x)
del TheTuble

# day-17-
Tuble=(9,)*4
print(Tuble)
if 9 in Tuble:
    print("true")
x=(3,6,9,12,15)
x=x+(2,4,6,8)
print(x)
print(len(x))
this_Tuble=((3,4,5,6))
this_Tuble=tuple(this_Tuble)
print(this_Tuble)



