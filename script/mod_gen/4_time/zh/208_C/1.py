def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = [K // N for i in range(N)]
    K %= N
    for i in range(K):
        ans[A[i] - 1] += 1
    for i in range(N):
        print(ans[i])
solve()
