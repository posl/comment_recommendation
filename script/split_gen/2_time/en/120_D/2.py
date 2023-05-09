def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    parent = [i for i in range(N + 1)]
    size = [1] * (N + 1)
    for i in range(1, M):
        a, b = AB[i]
        if find(a, parent) != find(b, parent):
            ans[i] = ans[i - 1] - size[find(a, parent)] * size[find(b, parent)]
            unite(a, b, parent, size)
        else:
            ans[i] = ans[i - 1]
    ans.reverse()
    print(*ans, sep='
')
