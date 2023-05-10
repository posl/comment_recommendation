def get_area(a, b, c):
    return abs((b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1]))
n = int(input())
points = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            area = get_area(points[i], points[j], points[k])
            if area > 0:
                count += 1
print(count)
