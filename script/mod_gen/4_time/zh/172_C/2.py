def solve():
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in range(1,N):
        A[i] += A[i-1]
    for i in range(1,M):
        B[i] += B[i-1]
    ans = 0
    j = M
    for i in range(N+1):
        if A[i] > K:
            break
        while B[j-1] > K - A[i]:
            j -= 1
        ans = max(ans,i+j)
    print(ans)

if __name__ == '__main__':
    solve()