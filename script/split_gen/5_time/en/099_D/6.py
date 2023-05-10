def main():
    n,c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    cc = [list(map(int, input().split())) for _ in range(n)]
    cc0 = [[0 for _ in range(c)] for _ in range(3)]
    for i in range(n):
        for j in range(n):
            cc0[(i+j)%3][cc[i][j]-1] += 1
    ans = float('inf')
    for i in range(c):
        for j in range(c):
            if i==j:
                continue
            for k in range(c):
                if i==k or j==k:
                    continue
                tmp = 0
                for l in range(c):
                    tmp += cc0[0][l]*d[l][i]
                    tmp += cc0[1][l]*d[l][j]
                    tmp += cc0[2][l]*d[l][k]
                ans = min(ans, tmp)
    print(ans)
