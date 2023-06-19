def get_the_lost_number(n, l):
    # 1 <= n <= 10^5
    # 1 <= A_i <= n (1 <= i <= 4N - 1)
    # 1 <= k <= N, 最多只有4个指数i，使A_i = k
    # 所以，如果一个数出现了3次，那么这个数就是被拿走的那个数
    l.sort()
    for i in range(0, 4*n-1, 2):
        if l[i] != l[i+1]:
            return l[i]
    return l[-1]
