def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    ans = 0
    t = 0
    for i in range(2*N):
        t += A[i]
        if i >= N:
            t -= A[i-N]
        if i >= N-1:
            ans = max(ans, t)
    print(ans)
solve()
