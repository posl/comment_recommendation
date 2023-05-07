def main():
    n, q = map(int, input().split())
    n -= 1
    edge = [[] for _ in range(n)]
    for _ in range(n):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    cnt = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        cnt[p-1] += x
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if u == 0:
                continue
            cnt[u-1] += cnt[v]
            stack.append(u)
    print(*cnt)
main()
