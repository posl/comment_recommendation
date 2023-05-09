def main():
    n,k,a = map(int, input().split())
    cards = k//n
    if k%n >= a:
        cards += 1
    print(cards)

if __name__ == '__main__':
    main()