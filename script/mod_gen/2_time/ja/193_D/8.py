def main():
    K = int(input())
    S = input()
    T = input()
    # 高橋君の手札
    S_cards = [0] * 9
    # 青木君の手札
    T_cards = [0] * 9
    for i in range(4):
        S_cards[int(S[i]) - 1] += 1
        T_cards[int(T[i]) - 1] += 1
    # まだ引いていないカードの枚数
    unused_cards = [K] * 9
    for i in range(9):
        unused_cards[i] -= S_cards[i] + T_cards[i]
    # 高橋君の勝ち数
    win = 0
    # 高橋君の手札に入れるカード
    for i in range(9):
        # 青木君の手札に入れるカード
        for j in range(9):
            if i == j:
                continue
            # 高橋君の手札に入れるカードと青木君の手札に入れるカードが同じ数字の場合
            if i == j:
                continue
            # 高橋君の手札に入れるカードと青木君の手札に入れるカードが同じ数字の場合
            if i == j:
                continue
            # 高橋君の手札に入れるカードと青木君の手札に入れるカードが同じ数字の場合
            if i == j:
                continue
            # 高橋君の手札に入れるカードと青木君の手札に入れるカードが同じ数字の場合
            if i == j:
                continue
            # 高橋君の手札に入れるカードと青木君の手札に入れるカードが同じ数字の場合
            if i == j:

if __name__ == '__main__':
    main()