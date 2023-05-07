def main():
    # input
    N, M = map(int, input().split())
    ABs = [[0, 0] for _ in range(N)]
    for i in range(N):
        ABs[i] = list(map(int, input().split()))
    # compute
    ABs.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if ABs[i][1] >= M:
            ans += ABs[i][0]*M
            break
        else:
            ans += ABs[i][0]*ABs[i][1]
            M -= ABs[i][1]
    # output
    print(ans)

if __name__ == '__main__':
    main()