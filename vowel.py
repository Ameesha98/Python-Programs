message=input("Enter a string")
mess=""
for i in message:
    if(i in ("aeiouAEIOU")):
        continue
    else:
        mess=mess+i;
print(mess)
