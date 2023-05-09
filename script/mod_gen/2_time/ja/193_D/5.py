def main():
    k = int(input())
    s = input()
    t = input()
    s = list(map(int, s[:4]))
    t = list(map(int, t[:4]))
    # print(s)
    # print(t)
    # print(k)
    s_score = 0
    t_score = 0
    for i in range(1, 10):
        s_score += i * 10 ** s.count(i)
        t_score += i * 10 ** t.count(i)
    # print(s_score)
    # print(t_score)
    # カードの枚数をリストに格納
    cards = [k] * 10
    for i in range(4):
        cards[s[i]] -= 1
        cards[t[i]] -= 1
    # print(cards)
    # どちらの手札にも含まれないカードの枚数を求める
    score_cards = 0
    for i in range(1, 10):
        score_cards += cards[i]
    # print(score_cards)
    # 両者の手札の点数を求める
    s_score_2 = 0
    t_score_2 = 0
    for i in range(1, 10):
        s_score_2 += i * 10 ** (s.count(i) + 1)
        t_score_2 += i * 10 ** (t.count(i) + 1)
    # print(s_score_2)
    # print(t_score_2)
    # 両者の手札の点数を求める
    s_score_3 = 0
    t_score_3 = 0
    for i in range(1, 10):
        s_score_3 += i * 10 ** (s.count(i) + 2)
        t_score_3 += i * 10 ** (t.count(i) + 2)
    # print(s_score_3)
    # print(t_score_3)
    # 両者の手札の点数を求める
    s_score_4 = 0
    t_score_4 = 0
    for i in range(1, 10):
        s_score_4 += i * 10 ** (

if __name__ == '__main__':
    main()