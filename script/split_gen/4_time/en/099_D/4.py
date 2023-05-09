def main():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]
    d0 = [[0 for _ in range(c)] for _ in range(3)]
    for i in range(n):
        for j in range(n):
            d0[(i+j)%3][c[i][j]-1] += 1
    ans = 10**10
    for i in range(c):
        for j in range(c):
            for k in range(c):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(c):
                    tmp += d0[0][l] * d[l][i]
                    tmp += d0[1][l] * d[l][j]
                    tmp += d0[2][l] * d[l][k]
                ans = min(ans, tmp)
    print(ans)
