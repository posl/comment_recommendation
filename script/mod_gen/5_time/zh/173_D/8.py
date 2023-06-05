def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    ans = 0
    for i in range(N):
        ans += A[i]
    if N == 2:
        print(ans)
        return
    s = 0
    for i in range(N):
        s += A[i]
    t = s
    for i in range(N, 2*N):
        s += A[i]
        s -= A[i-N]
        if s < t:
            t = s
    print(ans - t)
solve()
