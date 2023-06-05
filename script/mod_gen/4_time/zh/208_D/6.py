def main():
    n,m = map(int,input().split())
    A = []
    B = []
    C = []
    for i in range(m):
        a,b,c = map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    for i in range(m):
        A[i] -= 1
        B[i] -= 1
    INF = 10**9
    d = [[INF for i in range(n)] for j in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(m):
        d[A[i]][B[i]] = C[i]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    ans = 0
    for s in range(n):
        for t in range(n):
            for k in range(n):
                if d[s][t] == d[s][k] + d[k][t]:
                    ans += d[s][t]
    print(ans)

if __name__ == '__main__':
    main()