def main():
    N, Q = map(int, input().split())
    a = [0] * (N - 1)
    b = [0] * (N - 1)
    for i in range(N - 1):
        a[i], b[i] = map(int, input().split())
    p = [0] * Q
    x = [0] * Q
    for i in range(Q):
        p[i], x[i] = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        G[a[i]].append(b[i])
        G[b[i]].append(a[i])
    #print(G)
    #print(p)
    #print(x)
    counter = [0] * (N + 1)
    for i in range(Q):
        counter[p[i]] += x[i]
    #print(counter)
    stack = [1]
    visited = [0] * (N + 1)
    visited[1] = 1
    while stack:
        v = stack.pop()
        for w in G[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(w)
                counter[w] += counter[v]
    print(*counter[1:])

if __name__ == '__main__':
    main()