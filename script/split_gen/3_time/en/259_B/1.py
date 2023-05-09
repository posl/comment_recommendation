def rotate(a,b,d):
    import math
    d = math.radians(d)
    x = a * math.cos(d) - b * math.sin(d)
    y = a * math.sin(d) + b * math.cos(d)
    return x, y
a, b, d = input().split()
a = int(a)
b = int(b)
d = int(d)
x, y = rotate(a,b,d)
print(x, y)
