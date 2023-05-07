def main():
    N, M = map(int, input().split())
    e = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        e[u-1].append(v-1)
        e[v-1].append(u-1)
    if M != N - 1:
        print('No')
        return
    for i in range(N):
        if len(e[i]) != 2:
            print('No')
            return
    print('Yes')
