dec=44
print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal")
binary=input("Enter number in binary format")
decimal=int(binary,2);
print(binary,"in decimal=",decimal);
print(binary,"octal=",oct(binary));
print(binary,"in hex=",hex(binary));
