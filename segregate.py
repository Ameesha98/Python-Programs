#Ques1 segregate 0s and 1s
arr1=[1,0,1,0,1,0,1,0,1]
cnt=0
for i in arr1:
    if(i==1):
        arr1.append(1)
        del arr1[cnt]
    cnt+=1
print (arr1)
    
