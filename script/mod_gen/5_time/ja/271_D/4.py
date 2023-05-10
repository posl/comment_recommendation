def main():
    N,S = map(int,input().split())
    cards = []
    for i in range(N):
        cards.append(list(map(int,input().split())))
    #print(cards)
    for i in range(2**N):
        sum = 0
        temp = i
        card = []
        for j in range(N):
            card.append(temp%2)
            temp = temp//2
        #print(card)
        for k in range(N):
            if card[k] == 0:
                sum += cards[k][0]
            else:
                sum += cards[k][1]
        if sum == S:
            print("Yes")
            for k in range(N):
                if card[k] == 0:
                    print("T",end="")
                else:
                    print("H",end="")
            print("")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()