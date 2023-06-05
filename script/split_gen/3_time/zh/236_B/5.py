def solution():
    n = int(input())
    cards = {}
    for i in range(4*n-1):
        card = int(input())
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    for k, v in cards.items():
        if v % 2 == 1:
            print(k)
            break
