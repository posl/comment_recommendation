Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solution():
    pass

=======
Suggestion 2

def get_input():
    n, k = map(int, input().split())
    seg = []
    for i in range(k):
        seg.append(list(map(int, input().split())))
    return n, k, seg

=======
Suggestion 3

def main():
    # 读入数据
    N, K = map(int, input().split())
    # 读入K个区间
    # 区间按照左端点排序
    intervals = []
    for i in range(K):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort()
    # dp[i]表示到达i的方案数
    dp = [0] * (N+1)
    dp[1] = 1
    # 遍历区间
    for i in range(K):
        L, R = intervals[i]
        # 计算区间[L, R]的方案数
        # 从左到右遍历每个位置
        # 如果当前位置是区间的左端点，那么它的方案数就是dp[L]
        # 如果当前位置不是区间的左端点，那么它的方案数就是dp[L] + dp[L+1] + ... + dp[R]
        # 为了防止重复计算，我们可以用一个数组sum存储dp[L] + dp[L+1] + ... + dp[R]的值
        # 令sum[i] = dp[L] + dp[L+1] + ... + dp[i]
        # 那么sum[i+1] = sum[i] + dp[i+1]
        # 这样我们就可以用sum[R] - sum[L-1]来计算区间[L, R]的方案数
        sum = [0] * (N+1)
        sum[0] = dp[0]
        for j in range(1, N+1):
            sum[j] = sum[j-1] + dp[j]
        # 计算区间[L, R]的方案数
        # sum[R] - sum[L-1]
        dp[L] = sum[R] - sum[L-1]
        # 防止dp[L]为负数
        dp[L] %= 998244353
        # 更新dp
        for j in range(L+1, R+1):
            dp[j] = 0
    # 打印结果

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def problems179_d():
    pass

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    lr = []
    for i in range(k):
        lr.append(list(map(int, input().split())))
    dp = [0]*n
    dp[0] = 1
    for i in range(n):
        for j in range(k):
            if i + lr[j][0] < n:
                dp[i+lr[j][0]] += dp[i]
            if i + lr[j][1] + 1 < n:
                dp[i+lr[j][1]+1] -= dp[i]
    dp = dp[:-1]
    for i in range(1, n):
        dp[i] += dp[i-1]
    print(dp[-1]%998244353)

main()

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    S = set()
    for i in range(K):
        for j in range(L[i], R[i] + 1):
            S.add(j)

    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        for j in S:
            if i - j < 1:
                break
            dp[i] += dp[i - j]
            dp[i] %= 998244353

    print(dp[N])

=======
Suggestion 8

def get_input():
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    lr = []
    for i in range(k):
        lr.append(input().split())
    return n, k, lr

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            li = i - R[j]
            ri = i - L[j]
            if ri < 0:
                continue
            li = max(li, 1)
            dp[i] += dpsum[ri] - dpsum[li - 1]
        dp[i] %= 998244353
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= 998244353
    print(dp[N])
