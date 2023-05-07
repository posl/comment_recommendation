def main():
    N = int(input())
    E = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        E[u].append((v, w))
        E[v].append((u, w))
    ans = [None] * (N + 1)
    stack = [(1, 0)]
    while stack:
        v, p = stack.pop()
        if ans[v] is None:
            ans[v] = p
            for nv, w in E[v]:
                stack.append((nv, p ^ (w % 2)))
    print(*ans[1:], sep='
')

if __name__ == '__main__':
    main()