def area(x1, y1, x2, y2, x3, y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if area(x1, y1, x2, y2, x3, y3) != 0:
                ans += 1
print(ans)

if __name__ == '__main__':
    area()