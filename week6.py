# Week-6-
# دالة ترجع قيمة
from typing import Any, Union


def numb (x):
    return 2*x
#دالة طباعة قيم مصفوفة
def even2 (i):
    for y in i:
        print(y)
 # في حالة توفر عدد معاملات أجهله أستخدم *
def my_function (*kide):
    print(kide[0])
# دالة تستدعي نفسها
def MyF (k):
    if(k>0):
       result=k+MyF(k-1)
       print(result)
    else:
        result=0
    return result
def WithLambda (r):
    return lambda s:s*r

num=[2,4,6,8,10]
even2(num)
print(numb(2))
my_function("lila","jod","thamer")
print("-----------------------------")
MyF(5)

#دالة ليس لها إسم
F=lambda t:t*10
print(F(5))

I=lambda u,o,z:u+o*z
print(I(5,10,5))

StoreValue=WithLambda(9)
print(StoreValue(10))

MyArray=[2,4,6,8,10]
print(len(MyArray))
MyArray[1]=12
print(MyArray)
MyArray.append(14)
MyArray.pop(1)
even2(MyArray)



print("-------------------------")
print("Week Challenge")

def Power_fanction(N,P):
    if N>0:
         result=N**P
    else:
        result=0
    return result
print(Power_fanction(5,3))

MainList=[-4,-6,-5,-1,2,3,7,9,88]
PositiveList=[]
P_L=lambda n:n>0
for x in MainList:
    if P_L(x):
        PositiveList.append(x)

print(PositiveList)









