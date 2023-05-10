def main():
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**18
    cost = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        cost[i][i] = 0
    for A, B, C in ABC:
        cost[A][B] = C
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if i == j or j == k or k == i:
                    continue
                ans += cost[i][j] + cost[j][k] + cost[k][i]
    print(ans)

if __name__ == '__main__':
    main()