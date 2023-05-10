def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    ans = [0]*N
    ans[0] = 1
    stack = [0]
    while stack:
        v = stack.pop()
        c = 1
        for u in G[v]:
            if ans[u] != 0:
                continue
            if c == ans[v]:
                c += 1
            ans[u] = c
            c += 1
            stack.append(u)
    print(max(ans))
    for i in range(N-1):
        print(ans[i])

if __name__ == '__main__':
    main()