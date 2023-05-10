def distance(x1,x2,y1,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)
n = int(input())
coordinates = []
for _ in range(n):
    coordinates.append(list(map(int, input().split())))
