def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    bridge = [0] * N
    bridge[0] = 1
    for i in range(M-1, -1, -1):
        a = A[i] - 1
        b = B[i] - 1
        if bridge[a] == 1 and bridge[b] == 0:
            bridge[b] = 1
    bridge = bridge[::-1]
    # print(bridge)
    for i in range(1, N):
        bridge[i] += bridge[i-1]
    # print(bridge)
    for i in range(M):
        a = A[i] - 1
        b = B[i] - 1
        if bridge[b] - bridge[a] == 0:
            print(bridge[-1] * (bridge[-1]-1) // 2)
        else:
            print(bridge[-1] * (bridge[-1]-1) // 2 - (bridge[b] - bridge[a]) * (bridge[b] - bridge[a] - 1) // 2)
solve()
