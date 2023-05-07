def solve():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    #print(G)
    ans = [0] * N
    ans[0] = 1
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if ans[nv] == 0:
                ans[nv] = v+1
                stack.append(nv)
    print(*ans)
solve()

if __name__ == '__main__':
    solve()