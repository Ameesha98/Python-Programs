dict={"can\'t":"cannot","won\'t":"would not","\'m":" am","\'s":" is","\'re":" are","\'ve":" have","\'d":" would","\'ll":" will","n\'t":" not"}
para=input("Enter paragraph\n")
for key in dict:
    para=para.replace(key,dict[key])
print (para)
        
