def getArea(x, y):
    return (x-1) * (y-1)
x, y = map(int, input().split())
print(getArea(x, y))
