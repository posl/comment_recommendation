def main():
    n = int(input())
    cards = []
    for _ in range(n):
        cards.append(input())
    if len(cards) == len(set(cards)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()