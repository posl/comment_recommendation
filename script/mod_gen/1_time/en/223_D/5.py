def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        edge[A].append(B)
    dp = [0] * N
    for i in range(N):
        if dp[i] == 0:
            dp[i] = 1
            for j in edge[i]:
                if dp[j] == 0:
                    dp[j] = 2
                elif dp[j] == 1:
                    print(-1)
                    return
    ans = []
    for i in range(N):
        if dp[i] == 1:
            ans.append(i)
    for i in range(N):
        if dp[i] == 2:
            ans.append(i)
    print(*[i + 1 for i in ans])

if __name__ == '__main__':
    main()