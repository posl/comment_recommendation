def main():
    N = int(input())
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if xy[i][1] - xy[j][1] <= xy[i][0] - xy[j][0] <= xy[i][1] - xy[j][1]:
                ans += 1
            elif xy[i][1] - xy[j][1] >= xy[i][0] - xy[j][0] >= xy[i][1] - xy[j][1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()