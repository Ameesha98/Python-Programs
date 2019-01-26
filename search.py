message=input("Enter a string: ")
char=input("Enter char you want to find: ")
ind=0;
flag=0
for i in message:
    if(i==char):
        print("Present at index:",ind+1)
        flag=1
        break
    ind=ind+1
if(flag==0):
    print("Not found")
