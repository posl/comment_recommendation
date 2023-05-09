def main():
    n, q = map(int, input().split())
    # 1-indexed
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    # 1-indexed
    p = [0] * (n + 1)
    x = [0] * (n + 1)
    for _ in range(q):
        p_, x_ = map(int, input().split())
        p[p_] += x_
        x[p_] += x_
    ans = [0] * (n + 1)
    stack = [1]
    while stack:
        v = stack.pop()
        for w in g[v]:
            if ans[w] == 0:
                ans[w] = ans[v] + x[w]
                stack.append(w)
    print(*ans[1:])
