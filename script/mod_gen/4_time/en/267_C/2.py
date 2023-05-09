def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    C = [0]*(N+1)
    for i in range(N):
        C[i+1] = C[i] + i*A[i]
    D = [0]*(N+1)
    for i in range(N):
        D[i+1] = D[i] + A[i]
    for i in range(N):
        D[i+1] = max(D[i+1],D[i])
    ans = 0
    for i in range(N-M+1):
        ans = max(ans,C[i+M]-C[i]-B[i]*M+D[i])
    print(ans)
solve()

if __name__ == '__main__':
    solve()