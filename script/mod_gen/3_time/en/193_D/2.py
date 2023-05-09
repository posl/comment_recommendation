def solve():
    K = int(input())
    S = input()
    T = input()
    cards = [K] * 10
    for i in range(1, 10):
        cards[i] -= S[:4].count(str(i))
        cards[i] -= T[:4].count(str(i))
    takahashi = 0
    aoki = 0
    for i in range(1, 10):
        for j in range(1, 10):
            takahashi_cards = S[:4] + str(i)
            aoki_cards = T[:4] + str(j)
            if takahashi_cards.count(str(i)) > cards[i] or aoki_cards.count(str(j)) > cards[j]:
                continue
            takahashi_score = 0
            aoki_score = 0
            for k in range(1, 10):
                takahashi_score += k * 10 ** takahashi_cards.count(str(k))
                aoki_score += k * 10 ** aoki_cards.count(str(k))
            if takahashi_score > aoki_score:
                takahashi += cards[i] * cards[j]
            elif takahashi_score < aoki_score:
                aoki += cards[i] * cards[j]
    return takahashi / (takahashi + aoki)
print(solve())

if __name__ == '__main__':
    solve()