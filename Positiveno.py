a =[]
n = int(input("eneter the number of terms"))
for i in range(0,n):
    a.append(int(input("enter the term")))
print(a)
print("positive numbers are:")
for i in a:
    if i>0:
        print(i)
