def main():
    N = int(input())
    points = [list(map(int, input().split())) for i in range(N)]
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if points[i][0] == points[j][0] and points[j][0] == points[k][0]:
                    continue
                if points[i][1] == points[j][1] and points[j][1] == points[k][1]:
                    continue
                x = points[j][0] - points[i][0]
                y = points[k][1] - points[i][1]
                if points[i][0] + y >= points[k][0] and points[i][1] + x >= points[j][1]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()