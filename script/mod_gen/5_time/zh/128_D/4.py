def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            # print(i, j)
            # print(V[:i] + V[N-j:])
            ans = max(ans, sum(sorted(V[:i] + V[N-j:])[j:]))
    print(ans)

if __name__ == '__main__':
    solve()