def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    ans = [0] * N
    ans[0] = -1
    q = [0]
    while q:
        v = q.pop()
        for u in edges[v]:
            if ans[u] == 0:
                ans[u] = v + 1
                q.append(u)
    if 0 in ans:
        print("No")
    else:
        print("Yes")
        print(*ans[1:], sep="
")

if __name__ == '__main__':
    main()