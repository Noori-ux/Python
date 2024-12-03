base=int(input("enter a number for the base: "))
height=int(input("enter a number for the height: "))

def areaOftriangle(base,height):
    totalArea= 0.5*base*height
    return totalArea
print(f"Area of triangle is {areaOftriangle(base,height)} ")
