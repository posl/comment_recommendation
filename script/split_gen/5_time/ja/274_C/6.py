def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*(2*N+1)
    for i in range(N):
        ans[A[i]] = i+1
    for i in range(2*N,0,-1):
        ans[i//2] = max(ans[i//2], ans[i]+1)
    for i in range(1,2*N+1):
        print(ans[i])
