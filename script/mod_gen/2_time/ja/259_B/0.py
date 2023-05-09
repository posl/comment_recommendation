def rotate(a,b,d):
    import math
    rad = math.radians(d)
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    return x,y
a,b,d = map(int, input().split())
x,y = rotate(a,b,d)
print(x,y)

if __name__ == '__main__':
    rotate()