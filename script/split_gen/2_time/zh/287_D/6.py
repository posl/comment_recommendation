def solve():
    N, M = map(int, input().split())
    if M == 0:
        print('No')
        return
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    edges.sort()
    if edges[0][0] != 1:
        print('No')
        return
    for i in range(1, M):
        if edges[i][0] != edges[i-1][1]:
            print('No')
            return
    print('Yes')
    return
