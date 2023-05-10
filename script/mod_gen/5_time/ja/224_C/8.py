def calc_area(a, b, c):
    return abs((a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0]))
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            area = calc_area(points[i], points[j], points[k])
            if area > 0:
                ans += 1
print(ans)

if __name__ == '__main__':
    calc_area()