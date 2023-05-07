def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    par = [-1]*N
    par[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if par[nv] == -1:
                par[nv] = v
                stack.append(nv)
    print('Yes')
    for p in par[1:]:
        print(p+1)

if __name__ == '__main__':
    main()