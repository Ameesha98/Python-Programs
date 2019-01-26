for i in range(0,6):
    j=0
    var="A"
    while(j<=i):
        print(var,end=" ")
        var=chr(ord(var[0])+1)
        j=j+1
    print("\n")
