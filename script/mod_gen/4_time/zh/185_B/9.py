def solve():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 从家出发
    now = 0
    bat = N
    for i in range(M):
        # 到达咖啡馆
        bat -= A[i] - now
        if bat <= 0:
            print('No')
            return
        # 充电
        bat += B[i] - A[i]
        bat = min(bat, N)
        now = B[i]
    # 回家
    bat -= T - now
    if bat <= 0:
        print('No')
        return
    print('Yes')
solve()
