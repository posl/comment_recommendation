def main():
    n = int(input())
    cards = input()
    print("Takahashi" if cards.index('1') % 2 == 0 else "Aoki")

if __name__ == '__main__':
    main()