def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    s = [0]
    for i in range(1, N + 1):
        s.append(s[i - 1] + p[i])
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, (s[i + K] - s[i]) / 2 + s[i])
    print(ans)

if __name__ == '__main__':
    solve()