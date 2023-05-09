def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append((b-1, i))
        G[b-1].append((a-1, i))
    C = [0] * (N-1)
    used = [0] * N
    Q = [0]
    while Q:
        v = Q.pop()
        c = 1
        for nv, i in G[v]:
            if C[i] != 0:
                continue
            if c == used[v]:
                c += 1
            C[i] = c
            used[nv] = c
            c += 1
            Q.append(nv)
    print(max(C))
    print('
'.join(map(str, C)))
main()
