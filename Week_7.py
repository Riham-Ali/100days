class OddNum:
    x=5
    y=7
    z=7+5

class Information:
    def __init__(self,name,job):
        self.name=name
        self.job=job

class ParentClass:
    def __init__(self,fname,lname):
        self.First=fname
        self.Last=lname
    def PrintInf(self):
        print(self.First,self.Last)

class ChildClass(ParentClass):
    def __init__(self,fname,lname,year):
         super().__init__(fname,lname)
         self.BirthDay=year
    def Welcome(self):
         print(self.BirthDay)

class MyNum:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
             x=self.a
             self.a +=1
             return x
        else:
            raise StopIteration





C1=OddNum
C2=Information("Riham","Programmer")
C2.job="Student"
C3=ChildClass("Riham","Ali",1998)

print(C1.z)
print(C2.name)
print(C2.job)
C3.PrintInf()
C3.Welcome()
del C2.job
del C1


Lecture=("Tree","Array","LinkedList","Queue")
K=iter(Lecture)
print(next(K))
print(next(K))
print(next(K))
print(next(K))
print("--------------")

Name="Riham"
MyN=iter(Name)
print(next(MyN))
print(next(MyN))
print(next(MyN))
print(next(MyN))
print(next(MyN))

for x in Lecture:
    print(x)
for y in Name:
    print(y)

MyClass=MyNum()
C4=iter(MyClass)

for x in C4:
    print(x)


print("---------------------------------")

class Library:
    def __init__(self,Book,Shelf):
        self.Book=Book
        self.Shelf=Shelf

class Scines_Section(Library):
    def __init__(self,Book,Shelf,Name):
        super().__init__(Book,Shelf)
        self.name=Name

L1=Scines_Section(300,45,"Phisics Book")
print(L1.Book)
print(L1.Shelf)
print(L1.name)
L1.Shelf=4
L1.Book=200
print(L1.Book)
print(L1.Shelf)





