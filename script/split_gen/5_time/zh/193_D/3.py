def solve(K, S, T):
    # 1. 先统计出现次数
    cnt = [K] * 10
    for i in range(4):
        cnt[int(S[i])] -= 1
        cnt[int(T[i])] -= 1
    # 2. 计算高桥得分
    score = 0
    for i in range(1, 10):
        score += i * 10 ** cnt[i]
    # 3. 计算高桥获胜的概率
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            # 3.1. 如果高桥的牌大于青木的牌
            if score > i * 10 ** K + j * 10 ** K:
                # 3.1.1. 如果高桥的牌大于青木的牌，且高桥的牌面朝下的数字大于青木的牌面朝下的数字
                if i > j and cnt[i] > 0 and cnt[j] > 0:
                    ans += cnt[i] * (cnt[j] - (i == j)) / (9 * K - 8) * (cnt[j] - 1) / (9 * K - 9)
                # 3.1.2. 如果高桥的牌大于青木的牌，且高桥的牌面朝下的数字等于青木的牌面朝下的数字
                elif i == j and cnt[i] > 1:
                    ans += cnt[i] * (cnt[i] - 1) / (9 * K - 8) * (cnt[i] - 2) / (9 * K - 9)
            # 3.2. 如果高桥的牌等于青木的牌
            elif score == i * 10 ** K + j * 10 ** K:
                # 3.2.1. 如果高桥的牌等于青木的牌，且高桥的牌面朝下的数字大于
