def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if (x1 - x2) * (y3 - y2) == (x3 - x2) * (y1 - y2):
                    print('Yes')
                    return
    print('No')
