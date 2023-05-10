def main():
    N = int(input())
    v = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, w, c = map(int, input().split())
        v[u - 1].append((w - 1, c))
        v[w - 1].append((u - 1, c))
    q = [0]
    color = [-1] * N
    color[0] = 0
    while q:
        p = q.pop()
        for w, c in v[p]:
            if color[w] == -1:
                color[w] = color[p] ^ c
                q.append(w)
    print(*color, sep="\n")
