def rotate(a,b,d):
    from math import sin,cos,radians
    x=a*cos(radians(d))-b*sin(radians(d))
    y=a*sin(radians(d))+b*cos(radians(d))
    return x,y
a,b,d=map(int,input().split())
print(*rotate(a,b,d))

if __name__ == '__main__':
    rotate()