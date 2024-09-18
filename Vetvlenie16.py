import math
x1 = int(input("x1:"))
x2 = int(input("x2:"))
y1 = int(input("y1:"))
y2 = int(input("y2:"))
r1 = int(input("r1:"))
r2 = int(input("r2:"))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
if distance <= r1 + r2 and distance >= abs(r1 - r2):
    print("YES")
else:
    print("NO")