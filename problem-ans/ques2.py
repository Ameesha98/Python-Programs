para=input("Enter paragraph\n")
list=para.split()
ans=[]
for i in range(len(list)):
    if list[i].lower() in str(list[i+1:]).lower() and len(list[i])==3:
        ans.append(list[i])
print ('\n'.join(ans))

    

    
