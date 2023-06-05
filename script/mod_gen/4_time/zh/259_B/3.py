def rotate(a,b,d):
    import math
    pi = math.pi
    d = d*pi/180
    a1 = a*math.cos(d) - b*math.sin(d)
    b1 = a*math.sin(d) + b*math.cos(d)
    return a1,b1
a,b,d = map(int,input().split())
a1,b1 = rotate(a,b,d)
print(a1,b1)

if __name__ == '__main__':
    rotate()