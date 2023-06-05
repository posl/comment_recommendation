def solve(s, k):
    n = len(s)
    # 从左到右，计算每个人在原始方向上是否快乐
    happy = [0] * n
    for i in range(1, n):
        if s[i - 1] == s[i]:
            happy[i] = 1
    # 从左到右，计算每个人在原始方向上的快乐累计值
    happy_sum = [0] * n
    happy_sum[0] = happy[0]
    for i in range(1, n):
        happy_sum[i] = happy_sum[i - 1] + happy[i]
    # 从右到左，计算每个人在反方向上是否快乐
    happy_rev = [0] * n
    for i in range(n - 2, -1, -1):
        if s[i + 1] == s[i]:
            happy_rev[i] = 1
    # 从右到左，计算每个人在反方向上的快乐累计值
    happy_rev_sum = [0] * n
    happy_rev_sum[n - 1] = happy_rev[n - 1]
    for i in range(n - 2, -1, -1):
        happy_rev_sum[i] = happy_rev_sum[i + 1] + happy_rev[i]
    # 从左到右，计算每个人经过k次操作后的快乐值
    happy_k = [0] * n
    for i in range(n):
        happy_k[i] = happy_sum[i]
        if i + k < n:
            happy_k[i] += happy_rev_sum[i + k]
    return max(happy_k)
