def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                    continue
                count += 1
    print(count)
