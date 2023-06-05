def solve():
    N, W = map(int, input().split())
    # 从0开始，所以要+1
    imos = [0] * (200001)
    for i in range(N):
        S, T, P = map(int, input().split())
        imos[S] += P
        imos[T] -= P
    for i in range(200001):
        if i > 0:
            imos[i] += imos[i - 1]
        if imos[i] > W:
            print("No")
            return
    print("Yes")
    return
