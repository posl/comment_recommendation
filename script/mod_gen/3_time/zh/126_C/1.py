def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1 / N
        else:
            j = 0
            while i * (2 ** j) < K:
                j += 1
            ans += (1 / N) * (0.5 ** j)
    print(ans)

if __name__ == '__main__':
    solve()