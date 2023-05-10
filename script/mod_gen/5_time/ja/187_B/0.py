def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
            if -1 <= slope and slope <= 1:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()