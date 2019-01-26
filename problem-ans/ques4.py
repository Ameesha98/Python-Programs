dict={"Mr. ":"","Mrs. ":"","Ms. ":""}
para=input("Enter paragraph\n")
for key in dict:
    para=para.replace(key,dict[key])
print (para)
        
