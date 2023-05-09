def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    c = [[c[i][j] - 1 for j in range(N)] for i in range(N)]
    cost = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            for k in range(C):
                cost[(i + j) % 3][k] += D[c[i][j]][k]
    ans = 10 ** 10
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

if __name__ == '__main__':
    main()