def main():
    n = int(input())
    cards = []
    for i in range(n):
        cards.append(input())
    for i in range(n):
        for j in range(i+1,n):
            if cards[i] == cards[j]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()