def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    C = []
    for i in range(N):
        c = []
        for j in range(N):
            if i == j:
                c.append(1)
            else:
                c.append(0)
        C.append(c)
    for i in range(M):
        C[A[i]-1][B[i]-1] = 1
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if C[j][i] == 1 and C[i][k] == 1:
                    C[j][k] = 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if C[i][j] == 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()