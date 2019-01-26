#to add to matrices
list1=[]
list2=[]
n=int(input("Enter n"))
m=int(input("Enter m"))
for i in range(n):
    list=[]
    for j in range(m):
        num=int(input("Enter element"))
        list.append(num)
    list1.append(list)
for i in range(n):
    list=[]
    for j in range(m):
        num=int(input("Enter element"))
        list.append(num)
    list2.append(list)
list3=[]
for i in range(n):
    list=[]
    for j in range(m):
        num=list1[i][j]+list2[i][j]
        list.append(num)
    list3.append(list)
print (list3)
