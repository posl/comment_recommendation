def main():
    cards = list(map(int, input().split()))
    if cards.count(cards[0]) == 3 or cards.count(cards[0]) == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()