def find_lost_card(N, cards):
    card_dict = {}
    for i in range(1, N + 1):
        card_dict[i] = 4
    for card in cards:
        card_dict[card] -= 1
    for card in card_dict:
        if card_dict[card] == 1:
            return card
N = int(input())
cards = list(map(int, input().split()))
print(find_lost_card(N, cards))
