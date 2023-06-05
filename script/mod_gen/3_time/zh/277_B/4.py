def main():
    n = int(input())
    cards = []
    for i in range(n):
        cards.append(input())
    cards.sort()
    flag = 0
    for i in range(n-1):
        if cards[i] == cards[i+1]:
            flag = 1
            break
    if flag == 1:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()