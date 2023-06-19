def main():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (c + d) % 2 == 0:
            print('Town')
        else:
            print('Road')
