def main():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]
    def calc():
        cnt = [[0] * c for _ in range(3)]
        for i in range(n):
            for j in range(n):
                cnt[(i + j) % 3][c[i][j] - 1] += 1
        cost = [[0] * c for _ in range(3)]
        for i in range(3):
            for j in range(c):
                for k in range(c):
                    cost[i][j] += cnt[i][k] * d[k][j]
        return cost
    cost = calc()
    ans = float('inf')
    for i in range(c):
        for j in range(c):
            if i == j:
                continue
            for k in range(c):
                if i == k or j == k:
                    continue
                ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

if __name__ == '__main__':
    main()