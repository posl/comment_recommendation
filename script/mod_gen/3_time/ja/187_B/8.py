def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    #print(points)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (points[i][1]-points[j][1])/(points[i][0]-points[j][0]) <= 1:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()