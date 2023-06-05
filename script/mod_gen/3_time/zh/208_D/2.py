def main():
    n,m = map(int,input().split())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        x,y,z = map(int,input().split())
        a[x-1][y-1] = z
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][k] and a[k][j]:
                    if a[i][j]:
                        a[i][j] = min(a[i][j],a[i][k]+a[k][j])
                    else:
                        a[i][j] = a[i][k]+a[k][j]
            ans += a[i][j]
    print(ans)

if __name__ == '__main__':
    main()