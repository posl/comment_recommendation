def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            for k in range(j + 1, n):
                xk, yk = points[k]
                s = abs((xj - xi) * (yk - yi) - (xk - xi) * (yj - yi))
                if s > 0:
                    ans += 1
    print(ans)
