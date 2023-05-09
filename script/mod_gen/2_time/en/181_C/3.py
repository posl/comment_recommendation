def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                a = (x2 - x1) * (y3 - y1)
                b = (x3 - x1) * (y2 - y1)
                if a == b:
                    print('Yes')
                    return
    print('No')
main()

if __name__ == '__main__':
    main()