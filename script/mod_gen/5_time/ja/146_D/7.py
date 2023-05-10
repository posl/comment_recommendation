def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n - 1)]
    # 隣接リスト作成
    g = [[] for _ in range(n)]
    for a, b in ab:
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    # 1 から BFS しつつ、色を決めていく
    ans = [0] * (n - 1)
    q = [0]
    used = set()
    while q:
        v = q.pop(0)
        c = 1
        used.add(c)
        for u in g[v]:
            if ans[u] != 0:
                used.add(ans[u])
            else:
                while c in used:
                    c += 1
                used.add(c)
                ans[u] = c
                q.append(u)
    print(len(used))
    for c in ans:
        print(c)

if __name__ == '__main__':
    main()