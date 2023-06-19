def getArea(a,b,c):
    return abs((a[0]-c[0])*(b[1]-c[1])-(b[0]-c[0])*(a[1]-c[1]))/2
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split())))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            area = getArea(points[i],points[j],points[k])
            if area != 0:
                ans += 1
print(ans)

if __name__ == '__main__':
    getArea()