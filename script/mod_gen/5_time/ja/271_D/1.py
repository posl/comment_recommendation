def card_sum():
    N, S = map(int, input().split())
    card_list = [list(map(int, input().split())) for _ in range(N)]
    for i in range(2**N):
        card_sum = 0
        card_H_T = []
        for j in range(N):
            if ((i >> j) & 1):
                card_sum += card_list[j][0]
                card_H_T.append("H")
            else:
                card_sum += card_list[j][1]
                card_H_T.append("T")
        if card_sum == S:
            print("Yes")
            print("".join(card_H_T))
            exit()
    print("No")
card_sum()
