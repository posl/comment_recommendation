def getArea(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area
a,b,c = map(int, input().split())
print(int(getArea(a,b,c)))
