def main():
    N = int(input())
    card = list(map(int,input().split()))
    card.sort()
    for i in range(4*N-1):
        if i%2 == 0:
            if card[i] != card[i+1]:
                print(card[i])
                break
main()

if __name__ == '__main__':
    main()