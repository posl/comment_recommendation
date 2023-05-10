def get_sum_of_cards(N, M, A, BC):
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    cards = A
    for i in range(M):
        b = BC[i][0]
        c = BC[i][1]
        for j in range(b):
            if cards[j] < c:
                cards[j] = c
            else:
                break
        cards.sort()
    return sum(cards)
