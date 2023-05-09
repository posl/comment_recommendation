def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    #print(edges)
    #print(n)
    #print(edges)
    tree = [[] for _ in range(n)]
    for u, v, w in edges:
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    #print(tree)
    ans = [0] * n
    ans[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in tree[v]:
            if ans[u] != 0:
                continue
            if w % 2 == 0:
                ans[u] = ans[v]
            else:
                ans[u] = 1 - ans[v]
            stack.append(u)
    print(*ans, sep='
')
