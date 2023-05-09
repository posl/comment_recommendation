def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, A[i+K-1]-A[i])
    print(ans)
