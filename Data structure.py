#Assinging elements to different list
a1 =[1,2,3,4]
print("1st list")
print(a1)
a2 =[]
n=len(a1)
for i in range(0,n):
   a2.append(a1[i])
print("second list")
print(a2)
#Accessing elements from a tuple
tup =(1,2,3,4)
print("tuple")
print(tup)
print(tup[0])
#Deleting different dictionary elements
dict ={"c++":"easy","java":"hard"}
print(dict)
t = input("enter the key value pair to b deleted:")
del dict[t]
print(dict)
