def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    from collections import deque
    Q = deque()
    Q.append(0)
    C = [-1]*N
    C[0] = 0
    while Q:
        v = Q.popleft()
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
    for c in C[1:]:
        print(c+1)
