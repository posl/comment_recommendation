def solve():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: sum(x), reverse=True)
    for i in range(N):
        if i < K:
            print('Yes')
        else:
            print('No')
    return 0
