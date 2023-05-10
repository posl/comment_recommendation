def main():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]
    s = [[0] * c for _ in range(3)]
    for i in range(n):
        for j in range(n):
            s[(i + j) % 3][c[i][j] - 1] += 1
    ans = float('inf')
    for i in range(c):
        for j in range(c):
            if i == j:
                continue
            for k in range(c):
                if i == k or j == k:
                    continue
                cost = 0
                for l in range(c):
                    cost += s[0][l] * d[l][i]
                    cost += s[1][l] * d[l][j]
                    cost += s[2][l] * d[l][k]
                ans = min(ans, cost)
    print(ans)

if __name__ == '__main__':
    main()