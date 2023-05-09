def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    cost = [[0, 0, 0] for _ in range(C)]
    for i in range(N):
        for j in range(N):
            cost[(c[i][j] - 1)][(i + j) % 3] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, D[i][j] * cost[j][0] + D[j][k] * cost[k][1] + D[k][i] * cost[i][2])
    print(ans)

if __name__ == '__main__':
    main()