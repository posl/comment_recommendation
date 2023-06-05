def area(a, b, c):
    return abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2
n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if area(points[i], points[j], points[k]) > 0:
                ans += 1
print(ans)

if __name__ == '__main__':
    area()