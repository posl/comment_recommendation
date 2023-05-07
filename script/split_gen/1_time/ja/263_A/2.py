def main():
    cards = list(map(int, input().split()))
    cards.sort()
    if (cards[0] == cards[1] == cards[2] and cards[3] == cards[4]) or (cards[0] == cards[1] and cards[2] == cards[3] == cards[4]):
        print('Yes')
    else:
        print('No')
