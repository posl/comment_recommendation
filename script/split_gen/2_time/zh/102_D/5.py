def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 前から累積和
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    # 二分探索
    ans = float('inf')
    for i in range(2, N - 1):
        # B[i]がPの累積和
        # B[N] - B[i]がQ,R,Sの累積和
        # 二分探索でPを探索
        # 二分探索でQ,R,Sの中で最大と最小を探索
        # 二分探索でP,Q,R,Sの中で最大と最小を探索
        p = B[i] // 2
        l = 0
        r = i
        while r - l > 1:
            m = (l + r) // 2
            if B[i] - B[m] >= p:
                l = m
            else:
                r = m
        q = B[l]
        r = B[i] - q
        s = B[N] - B[i]
        ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
        p = B[N] // 2
        l = i
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if B[m] - B[i] >= p:
                r = m
            else:
                l = m
        q = B[i] - B[l]
        r = B[N] - B[m]
        s = B[N] - B[i]
        ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)
