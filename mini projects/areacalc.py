print ("Area Calculator!!!")
shape=input("Enter a shape!!! Circle, Square, Rectangle or Triangle: ")
shape=shape.lower()
if shape=="circle" or shape=="c":
    radius=float(input("Enter radius of circle: "))
    area=3.14*radius*radius
    print ("Area of circle is: %.3f"%area)
elif shape=="square" or shape=="s":
    side=input("Enter side of square: ")
    area=int(side)*int(side)
    print ("Area of square is: %.3f"%area)
elif shape=="rectangle" or shape=="r":
    length=input("Enter length of rectangle: ")
    breadth=input("Enter breadth of rectangle: ")
    area=int(length)*int(breadth)
    print ("Area of rectangle is: %.3f"%area)
elif shape=="triangle" or shape=="t":
    base=input("Enter base of triangle: ")
    height=input("Enter height of triangle: ")
    area=int(base)*int(height)/2
    print ("Area of triangle is: %.3f"%area)
else:
    print ("Please enter a valid option!")

