def solve():
    # 读取数据
    N, p, q, r = map(int, input().split())
    A = list(map(int, input().split()))
    # 逆序累积和
    R = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        R[i] = max(R[i + 1], A[i])
    # 正序累积和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 二分查找
    ans = 'No'
    for i in range(1, N - 1):
        if p * i > q:
            break
        while True:
            j = N - 1
            while j > i and (S[j] - S[i]) * p > r:
                j -= 1
            if j <= i:
                break
            if (S[j] - S[i]) * p == r:
                if (S[j] - S[i]) * q == (S[i] - S[0]) * r:
                    ans = 'Yes'
                break
            if (S[j] - S[i]) * q > (S[i] - S[0]) * r:
                break
            if (S[j] - S[i]) * q == (S[i] - S[0]) * r:
                ans = 'Yes'
            if R[j] * q > (S[i] - S[0]) * r:
                break
            if R[j] * q == (S[i] - S[0]) * r:
                ans = 'Yes'
            break
    print(ans)
