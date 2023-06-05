def solve():
    N = int(input())
    cards = list(map(int, input().split()))
    cards.sort()
    #print(cards)
    for i in range(0, 4*N-1, 2):
        if cards[i] != cards[i+1]:
            print(cards[i])
            break
