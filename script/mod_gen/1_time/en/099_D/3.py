def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    mod = [0, 0, 0]
    for i in range(N):
        for j in range(N):
            mod[(i + j) % 3] += 1
    cost = [[0] * C for _ in range(3)]
    for i in range(C):
        for j in range(C):
            cost[0][i] += mod[0] * D[i][j]
            cost[1][i] += mod[1] * D[i][j]
            cost[2][i] += mod[2] * D[i][j]
    for k in range(C):
        for i in range(3):
            for j in range(C):
                cost[i][j] -= D[k][j] * mod[(i + k) % 3]
    ans = 10 ** 9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

if __name__ == '__main__':
    main()