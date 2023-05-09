def main():
    # read in the cards
    cards = list(map(int, input().split()))
    # sort the cards
    cards.sort()
    # check if the cards are a full house
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        print("Yes")
    elif cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()