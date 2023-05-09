def main():
    K = int(input())
    S = input()
    T = input()
    # 1~9の数字をそれぞれ何枚持っているか
    card = [K] * 9
    # 1~9の数字をそれぞれ何枚持っているか
    def count_card(card):
        cnt = 0
        for i in range(9):
            cnt += card[i] * (i + 1)
        return cnt
    # 1~9の数字をそれぞれ何枚持っているか
    def count_score(card):
        cnt = 0
        for i in range(9):
            cnt += card[i] * 10 ** (i + 1)
        return cnt
    # 1~9の数字をそれぞれ何枚持っているか
    def count_score2(card):
        cnt = 0
        for i in range(9):
            cnt += card[i] * (i + 1) * 10 ** (i + 1)
        return cnt
    # 1~9の数字をそれぞれ何枚持っているか
    def count_score3(card):
        cnt = 0
        for i in range(9):
            cnt += card[i] * (i + 1) * 10 ** (i + 1) * 10 ** (i + 1)
        return cnt
    # 1~9の数字をそれぞれ何枚持っているか
    def count_score4(card):
        cnt = 0
        for i in range(9):
            cnt += card[i] * (i + 1) * 10 ** (i + 1) * 10 ** (i + 1) * 10 ** (i + 1)
        return cnt
    # 1~9の数字をそれぞれ何枚持っているか
    def count_score5(card)

if __name__ == '__main__':
    main()