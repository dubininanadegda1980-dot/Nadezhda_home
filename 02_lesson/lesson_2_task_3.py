import math

def square(side):
    area = side * side
    return math.ceil(area)

side = 5
result = square(side)
print("площадь квадрата со стороной " + str(side) + ": " + str(result))