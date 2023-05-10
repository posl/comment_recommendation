def solve():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        c = set()
        for j in range(N):
            if (i >> j) & 1:
                c |= set(S[j])
        if len(c) == K:
            ans = max(ans, sum(1 for j in range(N) if (i >> j) & 1))
    print(ans)

if __name__ == '__main__':
    solve()