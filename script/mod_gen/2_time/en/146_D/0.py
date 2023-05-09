def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    C = [-1] * N
    C[0] = 0
    Q = [0]
    while Q:
        v = Q.pop()
        c = 0
        for w in G[v]:
            if C[w] != -1:
                continue
            while c == C[v]:
                c += 1
            C[w] = c
            c += 1
            Q.append(w)
    print(max(C)+1)
    for i in range(1, N):
        print(C[i]+1)

if __name__ == '__main__':
    main()