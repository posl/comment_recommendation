def solve(S):
    # 用来存储答案
    ans = 0
    # 从S中减去3的倍数
    for i in range(0, S // 3 + 1):
        # 减去3的倍数后，剩下的数
        s = S - 3 * i
        # 从s中减去2的倍数
        for j in range(0, s // 2 + 1):
            # 减去2的倍数后，剩下的数
            t = s - 2 * j
            # 如果剩下的数是1的倍数，那么就是答案
            if t % 1 == 0:
                ans += 1
    # 返回答案
    return ans
