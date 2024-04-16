#1] Write a Python Program find an area of a rectangle and perimeter of the rectangle.

len = float(input("Enter the length of the rectangle: "))
bdth = float(input("Enter the breadth of rectangle: "))

area = len * bdth
print(f"area of rectangle = {area}")

peri = (2*(len + bdth))
print(f"perimeter of rectangle = {peri}")