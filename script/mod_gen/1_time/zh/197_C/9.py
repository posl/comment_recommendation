def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1<<31
    for i in range(1<<N-1):
        x = 0
        y = 0
        for j in range(N):
            y |= A[j]
            if i>>j & 1:
                x ^= y
                y = 0
        x ^= y
        ans = min(ans, x)
    print(ans)
solve()
