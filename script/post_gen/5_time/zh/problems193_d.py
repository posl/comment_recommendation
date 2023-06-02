Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_score(cards):
    score = 0
    for i, c in enumerate(cards):
        if c == '#':
            break
        else:
            score += (i+1)*10**(int(c)-1)
    return score

=======
Suggestion 3

def main():
    print("Hello World!")

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    K = int(input())
    S = input()
    T = input()
    S = S[0:4] + S[5]
    T = T[0:4] + T[5]

    def score(s):
        score = 0
        for i in range(4):
            score += (i+1) * 10**s.count(str(i+1))
        return score

    def calc():
        s_score = score(S)
        t_score = score(T)
        if s_score > t_score:
            return 1
        elif s_score < t_score:
            return 0
        else:
            return 0.5

    # print(calc())
    # return

    def calc2():
        s_score = score(S)
        t_score = score(T)
        if S[4] == '#' and T[4] == '#':
            if s_score > t_score:
                return 1
            elif s_score < t_score:
                return 0
            else:
                return 0.5
        elif S[4] == '#' and T[4] != '#':
            if s_score > t_score:
                return 1
            elif s_score < t_score:
                return 0
            else:
                return 0.5
        elif S[4] != '#' and T[4] == '#':
            if s_score > t_score:
                return 1
            elif s_score < t_score:
                return 0
            else:
                return 0.5
        else:
            if s_score > t_score:
                return 1
            elif s_score < t_score:
                return 0
            else:
                return 0.5

    print(calc2())
    return

=======
Suggestion 6

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
