def solve():
    N = int(input())
    ans = []
    def f(N):
        if N == 1:
            ans.append(1)
            return
        f(N-1)
        ans.append(N)
        f(N-1)
    f(N)
    print(*ans)
solve()
