def rotate(x,y,d):
    import math
    theta = math.radians(d)
    x1 = x*math.cos(theta)-y*math.sin(theta)
    y1 = x*math.sin(theta)+y*math.cos(theta)
    return x1,y1
x,y,d = map(int,input().split())
x1,y1 = rotate(x,y,d)
print(x1,y1)

if __name__ == '__main__':
    rotate()