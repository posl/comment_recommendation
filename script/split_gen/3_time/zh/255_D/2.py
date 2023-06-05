def problems255_d():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # 二分探索
    def binary_search(x):
        # Aの要素をxにするために必要な操作回数
        cnt = 0
        for a in A:
            if a > x:
                cnt += a - x
            else:
                cnt += min(x - a, x)
        return cnt
    # 二分探索の範囲を決定
    left = 0
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if binary_search(mid) < binary_search(mid + 1):
            right = mid
        else:
            left = mid
    ans = []
    for x in X:
        ans.append(binary_search(x))
    print(*ans, sep='\n')
problems255_d()
