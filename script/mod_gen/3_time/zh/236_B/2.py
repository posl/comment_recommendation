def find_missing_card():
    N = int(input())
    cards = list(map(int, input().split()))
    cards.sort()
    if cards[0] != cards[1]:
        return cards[0]
    elif cards[-1] != cards[-2]:
        return cards[-1]
    else:
        for i in range(1, len(cards)-1):
            if cards[i] != cards[i-1] and cards[i] != cards[i+1]:
                return cards[i]
print(find_missing_card())
