def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A - 1].append(B - 1)
        G[B - 1].append(A - 1)
    ans = 0
    visited = [False] * N
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for u in G[v]:
                if visited[u]:
                    continue
                stack.append(u)
    print(ans)
main()

if __name__ == '__main__':
    main()