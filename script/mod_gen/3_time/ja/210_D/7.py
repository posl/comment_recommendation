def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    cost = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            cost[i][j] = A[i][j] + i + j
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, cost[i][j] + cost[k][l] + C * (abs(i-k) + abs(j-l)))
    print(ans)

if __name__ == '__main__':
    main()