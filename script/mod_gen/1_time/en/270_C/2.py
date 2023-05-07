def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    ans = [0]*N
    for i in range(N):
        if i == X:
            continue
        elif i == Y:
            continue
        else:
            dist = [float('inf')]*N
            dist[i] = 0
            Q = [i]
            while Q:
                v = Q.pop()
                for w in G[v]:
                    if dist[w] == float('inf'):
                        dist[w] = dist[v] + 1
                        Q.append(w)
            ans[dist[X] + dist[Y] + 1] += 1
    print(' '.join(map(str, ans[1:])))

if __name__ == '__main__':
    main()