def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    color = [0] * (N-1)
    used = [0] * (N+1)
    k = 0
    for v in range(N):
        c = 1
        for u in G[v]:
            if u < v:
                continue
            while used[c]:
                c += 1
            used[c] = 1
            color[u-1] = c
            k = max(k, c)
            c += 1
        for u in G[v]:
            if u < v:
                continue
            used[color[u-1]] = 0
    print(k)
    for c in color:
        print(c)

if __name__ == '__main__':
    main()