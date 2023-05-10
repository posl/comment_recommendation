def main():
    cards = [int(x) for x in input().split()]
    print(sum(cards) - min(cards))

if __name__ == '__main__':
    main()