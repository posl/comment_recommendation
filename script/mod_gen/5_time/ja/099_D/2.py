def main():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]
    rgb = [[0]*c for _ in range(3)]
    for i in range(n):
        for j in range(n):
            rgb[(i+j)%3][c[i][j]-1] += 1
    ans = float('inf')
    for i in range(c):
        for j in range(c):
            for k in range(c):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(c):
                    tmp += d[l][i]*rgb[0][l]
                    tmp += d[l][j]*rgb[1][l]
                    tmp += d[l][k]*rgb[2][l]
                ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()