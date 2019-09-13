# day-20-
print("+----------- DAY 20 ----------+")
TheSet = {"apple","orange","berry","apple"}
TheSet.add("banana")
TheSet.update([5,5,7])
for x in TheSet:
    print(x)

# day-21-
print("+----------- DAY 21 ----------+")
TheSet.remove(5)
x=TheSet.pop()
print(x)
print(len(TheSet))
del TheSet

# day-22-
print("+----------- DAY 22 ----------+")

menu = {"cupCake":10,
        "BlackCoffe":12,
        "IceCoffe":25}
x=menu.get("IceCoffe")
print(x)
menu["IceCoffe"]=28
for a in menu:
    print(a)

for a in menu:
    print(menu[a])

print(menu.values())

for i,w in menu.items():
    print(i,w)

# day-23 + 24-
print("+----------- DAY 23 + 24 ----------+")
NewMenu=menu.copy()
del menu
print(NewMenu)
Employee1 = {"Ahmed":25}
Employee2 = {"Omar":23}
Employee3 = {"Mohamed":27}
Employees = {"Employee1":Employee1,
             "Employee2":Employee2,
             "Employee3":Employee3}
print(Employees)

# day-25 + 26-
print("+----------- DAY 25 + 26 ----------+")
number = {1,3,5,7,8}
number.update([4,8,12])
number.remove(5)
print(number)
number.clear()

TheDict={"name":"pigeon",
         "type":"bired",
         "Skin Cover":"fealhers"}
x=TheDict["type"]
print(x)
TheDict[ "Skin Cover"]="non"
print(TheDict)