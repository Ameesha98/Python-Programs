'''try:
    a=int(input("Enter a positive number"))
    if(a<0):
        raise ValueError("This is not a positive integer.Please enter a positive integer only")
except ValueError as ve:
    print (ve)
try:
    f=open("nosuchfile.txt")
except:
    print("No such file exists")
    #raise'''
def linux_interaction():
    assert('linux' in sys.platform),"function can only run on linux systems"
    print('Doing something')	
try:
    linux_interaction()
except:
    pass
