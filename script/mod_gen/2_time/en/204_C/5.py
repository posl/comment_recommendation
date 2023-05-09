def main():
    n,m = map(int,input().split())
    path = [[0]*n for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        path[a-1][b-1] = 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if path[i][j] == 1:
                for k in range(n):
                    if j == k:
                        continue
                    if path[j][k] == 1:
                        if path[k][i] == 1:
                            ans += 1
    print(ans)

if __name__ == '__main__':
    main()