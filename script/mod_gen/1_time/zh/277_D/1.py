def main():
    [N, M] = [int(i) for i in input().split()]
    cards = [int(i) for i in input().split()]
    cards.sort()
    cards = cards[::-1]
    # print(cards)
    ans = 0
    for i in range(N):
        if cards[i] >= M:
            cards[i] = 0
            ans += 1
        else:
            break
    # print(cards)
    cards = cards[::-1]
    # print(cards)
    if len(cards) == 1:
        ans += cards[0]
    else:
        ans += cards[0]
        for i in range(1, len(cards)):
            if cards[i] >= cards[i-1]:
                cards[i] = cards[i-1] - 1
                if cards[i] < 0:
                    cards[i] = 0
                ans += cards[i]
            else:
                ans += cards[i]
    print(ans)

if __name__ == '__main__':
    main()