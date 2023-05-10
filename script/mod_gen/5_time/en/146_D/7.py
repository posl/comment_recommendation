def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        a, b = map(int, input().split())
        edges.append([a, b, i])
    adj = [[] for _ in range(N+1)]
    for a, b, i in edges:
        adj[a].append((b, i))
        adj[b].append((a, i))
    ans = [0] * (N-1)
    used = [False] * (N+1)
    used[1] = True
    color = 0
    for a, b, i in edges:
        if ans[i] != 0:
            continue
        color += 1
        ans[i] = color
        used_color = [False] * (N+1)
        used_color[ans[i]] = True
        stack = [(a, b), (b, a)]
        while stack:
            v, p = stack.pop()
            for nv, ni in adj[v]:
                if nv == p:
                    continue
                if ans[ni] != 0:
                    continue
                while used_color[color]:
                    color += 1
                ans[ni] = color
                used_color[color] = True
                stack.append((nv, v))
    print(max(ans))
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()