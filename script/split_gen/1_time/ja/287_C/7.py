def main():
    N, M = map(int, input().split())
    if M == 0:
        print('No')
        return
    if M != N - 1:
        print('No')
        return
    edge = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        edge[u-1].add(v-1)
        edge[v-1].add(u-1)
    for i in range(N):
        if len(edge[i]) != 2:
            print('No')
            return
    print('Yes')
    return
