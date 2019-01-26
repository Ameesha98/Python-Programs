message=input("Enter your message")
m=message[0]
var=message.replace(m,"$")
m=m+var[1:len(var)]
print (m)
