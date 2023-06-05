def rotate(a,b,d):
    import math
    d = math.radians(d)
    x = a*math.cos(d) - b*math.sin(d)
    y = a*math.sin(d) + b*math.cos(d)
    return x,y
a,b,d = map(int,input().split())
x,y = rotate(a,b,d)
print(x,y)

if __name__ == '__main__':
    rotate()