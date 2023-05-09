def main():
    n, s = map(int, input().split())
    cards = []
    for i in range(n):
        cards.append(list(map(int, input().split())))
    #print(cards)
    for i in range(2**n):
        #print(i)
        bi = bin(i)[2:].zfill(n)
        #print(bi)
        total = 0
        for j in range(n):
            if bi[j] == '0':
                total += cards[j][0]
            else:
                total += cards[j][1]
        #print(total)
        if total == s:
            print('Yes')
            for j in range(n):
                if bi[j] == '0':
                    print('T', end='')
                else:
                    print('H', end='')
            print()
            return
    print('No')

if __name__ == '__main__':
    main()