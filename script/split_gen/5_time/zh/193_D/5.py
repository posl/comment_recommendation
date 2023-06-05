def main():
    # 读入数据
    K = int(input())
    S = input()
    T = input()
    # 用于计数的数组
    cnt = [K] * 10
    # 用于计算牌面的函数
    def calc(cards):
        res = 0
        for i in range(1, 10):
            res += i * 10 ** cards[i]
        return res
    # 移除手牌中的数字
    def remove(cards, num):
        cards[num] -= 1
    # 高桥的得分
    score_s = 0
    # 青木的得分
    score_t = 0
    # 用于计算高桥的得分
    for i in range(4):
        num = ord(S[i]) - ord('0')
        remove(cnt, num)
        score_s += num * 10 ** cnt[num]
    # 用于计算青木的得分
    for i in range(4):
        num = ord(T[i]) - ord('0')
        remove(cnt, num)
        score_t += num * 10 ** cnt[num]
    # 用于计算高桥获胜的概率
    def calc_prob(score_s, score_t, cnt):
        res = 0
        for i in range(1, 10):
            for j in range(1, 10):
                # 如果高桥的得分大于青木的得分
                if score_s + i * 10 ** cnt[i] > score_t + j * 10 ** cnt[j]:
                    # 计算高桥获胜的概率
                    res += cnt[i] / (9 * K - 8) * (cnt[j] - (i == j)) / (9 * K - 9)
        return res
    # 计算高桥获胜的概率
    prob = calc_prob(score_s, score_t, cnt)
    # 打印结果
    print(prob)
