def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    c = [1] * (N + 1)
    for i in range(1, M):
        a, b = AB[i]
        if c[a] < c[b]:
            a, b = b, a
        ans[i] = ans[i - 1] - c[a] * c[b]
        c[a] += c[b]
    print(*ans[::-1], sep='
')
